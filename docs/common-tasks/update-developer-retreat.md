# Update the Developer Retreat page (once a year)

The page **https://openms.de/developer-retreat/** tells people about the next retreat and shows a photo of the last one. Once a year, after a retreat has finished, you update a few lines.

**You will change:** about 15 lines in `config.yaml` and upload up to 2 pictures  ·  **Time:** about 20 minutes  ·  **Skills needed:** none

## What you will change

**The "Upcoming retreat" block**

![The Upcoming retreat block with parts numbered](../images/update-developer-retreat/1-upcoming.png)

**The photo of the last retreat** (further down the same page)

![The past photo with its caption](../images/update-developer-retreat/2-past-photo.png)

**And the matching lines in `config.yaml`** (the numbers are the same):

![The retreat lines in config.yaml](../images/update-developer-retreat/3-config.png)

| Number | Lines | What it is |
|:--:|-------|-----------|
| 1 | each `text:` under `facts:` | The short lines with the date, place and registration note. You can add or delete a line. |
| 2 | `open:`, `url:`, `label:`, `closedHint:` | The registration button (see below). |
| 3 | `src:` under `poster:` | The poster picture. `alt:` right below is its description. |
| 4 | `src:` and `alt:` under `pastPhoto:` | The photo of the retreat that just happened, and its description. |
| 5 | `caption:` | The sentence under that photo. |

## Step by step

### Step 1 – Upload the new pictures

The new poster (and the photo of the retreat that just ended) go in the folder **`static/images/`**. See [Add images](add-images.md). Note the exact file names, for example `dev_retreat_2028_poster.png`.

### Step 2 – Open `config.yaml`

Open **https://github.com/OpenMS/OpenMS-website/blob/main/config.yaml**, click the **pencil icon**, click inside the text box, press **Ctrl + F** (Windows) or **Cmd + F** (Mac) and search for:

```
pastPhoto
```

([Need help?](../getting-started/edit-via-github.md#step-1--open-the-file))

### Step 3 – Move last year's retreat to "past"

- Under `pastPhoto:`: put in the photo of the retreat that just ended, its description (`alt`) and `caption`. Example:

  ```yaml
  pastPhoto:
    src: /images/dev_retreat_2027.jpeg
    alt: OpenMS contributors at the 2027 developer retreat in Portugal
    caption: 2027 Developer retreat at Resort Natura in the Algarve, Portugal
  ```

### Step 4 – Fill in the next retreat

- Under `facts:`, change the three `text:` lines. For example: `March 2028 (dates to be confirmed)`, `Location to be announced`, `Registration opens in early 2028`.
- Under `poster:`, change `src:` to the new poster file and `alt:` to its description. Not ready yet? Ask the web team before removing it.

### Step 5 – Registration button

| Situation | What to set |
|-----------|-------------|
| Registration **not open yet** | `open: false`. Write the message people see in `closedHint:`. |
| Registration **is open** | `open: true` and put the sign-up address in `url:` between the quotes, for example `url: "https://tally.so/r/abc123"`. |

### Step 6 – Save, send for review, and check

[How to make a change, steps 3 to 6](../getting-started/edit-via-github.md#step-3--save-commit-changes). In the **Deploy Preview**, add **/developer-retreat/** to the address and check:

- [ ] The dates and place are right.
- [ ] The poster shows and is not cut.
- [ ] The register button does what you expect.

> The retreat also shows in the **Community calendar**. See [Add or change an event](update-community-calendar.md).

## Parts that rarely change

`eyebrow`, `pageTitle`, `about` and `highlights` describe the retreat in general. You don't need to change them every year. Leave `headline` to the web team (it contains hidden formatting).

## Common mistakes

| What went wrong | How to fix it |
|-----------------|---------------|
| The preview says **Failed** | A `text:` line with a colon in it needs quotes: `text: "Dates: March 2028"`. See [Spaces matter](../getting-started/edit-via-github.md#spaces-matter-in-configyaml). |
| A picture is broken | The `src:` path must match the uploaded file exactly (capital letters count) and start with `/images/`. |
| The register button still says closed | `open:` must be `true` (no quotes) and `url:` must have an address. |

## Related guides

- [Add images](add-images.md)
- Back to the [list of all guides](../README.md)
