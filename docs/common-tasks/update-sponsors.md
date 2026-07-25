# Update sponsors (Our Sponsors page)

Sponsor logos are shown on the **[Our Sponsors](/our-sponsors/)** page (linked from the **About** menu in the navbar). The page is modelled after the [Apache sponsors page](https://www.apache.org/foundation/sponsors): a logo wall, with an "Interested in sponsoring us?" contact link at the bottom.

Everything is driven by `config.yaml` — no template changes are needed for day-to-day updates.

## Add a new sponsor

1. Add the logo file to `static/images/logos/` (SVG preferred, PNG is fine).
2. In `config.yaml`, find `params.aboutPage.sponsors` and append an entry:

```yaml
      sponsors:
        - name: Acme Corp                  # display name (fallback if the logo fails to load)
          url: https://acme.example/       # where clicking the logo goes
          logo: /images/logos/acme.svg     # path to the file you added in step 1
          alt: Acme Corp                   # accessible alt text
          logoOnDark: true                 # ONLY add this if the logo art is white/light —
                                           # it renders the tile with a dark background
          # tier: gold                     # optional — see "Sponsorship tiers" below
```

3. Preview locally (`make serve`, then open `/our-sponsors/`) and check the logo displays at a reasonable size and links correctly.

To **remove** a sponsor, delete its entry from the list. Order in the list = display order on the page.

## Edit the page text

Under `params.aboutPage.sponsorsSection` in `config.yaml`:

| Key | What it controls |
| --- | --- |
| `eyebrow` | Small label above the page title |
| `intro` | Lead sentence in the page hero |
| `listTitle` | Heading above the logo wall ("Sponsors include:") |
| `contactCta` | The "Interested in sponsoring us?…" line at the bottom |
| `contactUrl` | Where that line links (default `/contact/`) |

## Sponsorship tiers (for later)

We don't have enough sponsors per level to divide the wall into tiers yet, but the template is ready. When the time comes:

1. In `config.yaml`, set `params.aboutPage.sponsorsSection.groupByTier: true`.
2. Give each sponsor a `tier:` value matching an `id` from `params.sponsorTiers.levels` (`platinum`, `gold`, `silver`, `bronze`).

Tiers are rendered in the order defined in `sponsorTiers.levels`, and **only tiers that have at least one sponsor are shown** — empty levels are skipped automatically. Sponsors without a `tier` will not appear while grouping is on, so make sure every entry has one before enabling it.

## Where the code lives (web team)

- Page content: `content/en/our-sponsors.md` (front matter only)
- Page template: `layouts/partials/our-sponsors-main.html` (hero) and `layouts/partials/about-sponsors-section.html` (logo wall + tier template)
- Single logo tile: `layouts/partials/about-sponsor-logo.html`
- Styles: `assets/css/about.css` (`.about-sponsors-*`)
- Navbar entry: `config.yaml` → `navbar.links` → About → sublinks
