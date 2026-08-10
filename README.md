# AZ CPR Plus+

Marketing website build for AZ CPR Plus+, implemented as a static multi-page HTML/CSS site from approved design comps.

## Project Snapshot

- Project type: static multi-page website
- Stack: HTML5 + CSS3
- Pages implemented:
	- Home: `index.html`
	- Onsite / Group Training: `about.html`
	- Courses: `courses.html`
	- About & Contact: `contact.html`
- Brand assets (local):
	- `images/cpr-plus-logo.svg`
	- `images/Rob Leaky.png`

## Current Status

- [x] Core page structure complete
- [x] Global nav, footer, and cross-page linking in place
- [x] Contact + quote form layout implemented
- [x] Mobile responsiveness pass completed
- [x] Branding updated to AZ CPR Plus+
- [x] Contact details updated site-wide

## Local Preview

Because this is a static site, you can open pages directly in a browser:

1. Open `index.html` for the home page.
2. Navigate between pages using the site nav.

Optional local server (recommended):

```powershell
# from project root
python -m http.server 5500
```

Then open:

`http://localhost:5500/index.html`

## Client Review Workflow

Recommended process for stakeholder updates:

1. Make changes in the project files.
2. Commit with a clear message.
3. Push to `main`.
4. Record what changed in `CLIENT-UPDATES.md`.
5. Share the latest commit or repository link with the client.

## Repository Structure

```text
.
├── about.html
├── contact.html
├── courses.html
├── index.html
├── styles.css
├── images/
│   ├── cpr-plus-logo.svg
│   └── Rob Leaky.png
└── CLIENT-UPDATES.md
```

## Notes

- Figma-exported remote assets were progressively replaced with local assets for primary branding and key content imagery.
- `styles.css` centralizes shared tokens, layout rules, and page-specific sections.