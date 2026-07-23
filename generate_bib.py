import re
import requests
import pandas as pd
from Bio import Entrez
from datetime import datetime

# This script fetches the NCBI collection for OpenMS that is manually created and updates the references on the website acordingly. 

# Set email address (required by NCBI)
Entrez.email = "your_email@domain.com"

COLLECTION_URL = "https://pubmed.ncbi.nlm.nih.gov/collections/67464722/public/"

def get_collection_pmids(url):
    """Scrape the PMIDs out of a public PubMed 'My NCBI' collection page."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    # The page embeds a hidden 'saved search' field containing every PMID
    # in the collection as a comma-separated list ending in "[uid]"
    match = re.search(r'([\d,]{20,})\[uid\]', resp.text)
    if not match:
        raise ValueError("Could not find PMID list in collection page — "
                          "the page structure may have changed.")

    pmids = match.group(1).strip(",").split(",")
    return pmids

print("Fetching PMIDs from public collection...")
pmids = get_collection_pmids(COLLECTION_URL)
print(f"Found {len(pmids)} publications in the collection")

# Fetch full records for each paper
citations_data = []
for pubmed_id in pmids:
    try:
        handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="xml")
        xml_record = Entrez.read(handle)
        handle.close()

        if xml_record and len(xml_record.get("PubmedArticle", [])) > 0:
            citation = xml_record["PubmedArticle"][0]["MedlineCitation"]
            article = citation.get("Article", {})

            title = str(article.get("ArticleTitle", "")).rstrip(".")

            # Authors
            authors_list = article.get("AuthorList", [])
            authors = ", ".join(
                f"{a.get('LastName', '')} {a.get('Initials', '')}".strip()
                for a in authors_list if a.get('LastName')
            )

            # Journal
            journal = article.get("Journal", {}).get("Title", "")

            # Year — check ArticleDate first, fall back to JournalIssue PubDate,
            # and finally MedlineDate for odd formats (e.g. "2020 Jan-Feb")
            year = None
            pub_date = article.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {})
            if "Year" in pub_date:
                year = pub_date["Year"]
            elif "MedlineDate" in pub_date:
                year_match = re.search(r"\d{4}", pub_date["MedlineDate"])
                if year_match:
                    year = year_match.group(0)

            if title and year:
                citations_data.append({
                    "Title": title,
                    "Authors": authors,
                    "Publication": journal,
                    "Year": int(year),
                    "PubMedID": pubmed_id,
                })
    except Exception as e:
        print(f"Error processing PMID {pubmed_id}: {e}")
        continue

# Build dataframe
citations = pd.DataFrame(citations_data)
citations.drop_duplicates(subset=["PubMedID"], inplace=True)
citations.sort_values("Year", ascending=False, inplace=True)

print(f"Successfully processed {len(citations)} of {len(pmids)} publications")

# Generate markdown
with open("content/en/publications.md", "w") as file:
    file.write("# List of OpenMS Publications\n\n")
    for year, year_citations in citations.groupby("Year", sort=False):
        year = int(year)
        file.write(f"## {year}\n")
        for _, citation in year_citations.sort_values("Title").iterrows():
            url = f" [Link](https://www.ncbi.nlm.nih.gov/pubmed/{citation['PubMedID']})"
            entry = f"- {citation['Authors']} *{citation['Title']}*. {citation['Publication']}. {year}{url}"
            file.write("\n\n" + entry)
        file.write("\n***\n")

print("Publications written to content/en/publications.md")
