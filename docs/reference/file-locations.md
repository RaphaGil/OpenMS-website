# File locations — quick lookup

“I want to change X” → edit Y.

## Content (Markdown)

| What | Where |
|------|--------|
| News article | `content/en/news/<slug>.md` |
| News listing intro | `content/en/news/_index.md` |
| About, governance, legal, etc. | `content/en/<name>.md` |
| Key features detail pages | `content/en/keyfeatures/*.md` |

## Configuration

| What | Where |
|------|--------|
| Homepage hero | `config.yaml` → `params.hero` |
| Homepage big numbers | `config.yaml` → `params.homeMetrics` |
| News banner (top strip) | `config.yaml` → `params.newsBanner` |
| News page labels / filter | `config.yaml` → `params.newsSection` |
| Key features (“What is OpenMS?”) | `config.yaml` → `params.keyfeatures` |
| Featured Apps (home page and `/featured-apps/`) | `config.yaml` → `params.webapps` |
| Affiliated Apps | `config.yaml` → `params.affiliateProjects` |
| “Adopted by labs and institutions” logos | `config.yaml` → `params.universityPartners` |
| Sponsors (`/our-sponsors/`) | `config.yaml` → `params.aboutPage.sponsors` |
| Developer Retreat page | `config.yaml` → `params.developerRetreatPage` |
| Publications list | `pmids.txt` |
| Community calendar events | `data/community_events.yaml` |
| Community calendar page | `content/en/calendar.md`, `layouts/partials/community-calendar-main.html` |
| Donate page (Zeffy) | `content/en/donate.md`, `layouts/partials/donate-main.html`, `config.yaml` → `params.donatePage` |
| Navbar & footer | `config.yaml` → `params.navbar`, `params.footer` |
| Site URL, theme, analytics | `config.yaml` (top) |

## Images & static files

| What | Where |
|------|--------|
| Any static asset | `static/` → URL `/...` |
| Logos | `static/images/logos/` |
| Webapp logos | `static/images/webapp/logo/` |
| Affiliated App logos | `static/images/webapp/logo/affiliate/` |
| News pictures | `static/images/news_images/` |

## Layout & style (web team)

| What | Where |
|------|--------|
| Homepage section order | `layouts/index.html` |
| News list / article layout | `layouts/news/` |
| Homepage partials | `layouts/partials/` (hero, webapps, news-banner, …) |
| Site CSS (base) | `assets/css/*.css` |
| Page-specific CSS (loads last) | `assets/css/overrides/<page>.css` |
| Custom shortcodes | `layouts/shortcodes/` |
| Base theme | `themes/scientific-python-hugo-theme/` (avoid editing) |

## Build & deploy

| What | Where |
|------|--------|
| Local build commands | `Makefile` |
| Hugo version for Netlify | `netlify.toml` |
| Maintainer docs | `docs/` (this folder) |

## Hardcoded content (needs code change today)

| What | Where |
|------|--------|
| Sponsor logos on About (`{{< sponsors >}}`) | `layouts/shortcodes/sponsors.html` |
| The Contact block at the bottom of the home page | `layouts/partials/contact-area.html` |
| Most governance / press-kit page wording | `layouts/partials/governance-main.html`, `press-kit-main.html` |

For a plain-language tour, see the [map of the repository](../getting-started/repo-map.md).
