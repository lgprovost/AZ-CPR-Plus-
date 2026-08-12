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
- Brand and content assets:
  - `images/cpr-plus-logo3.svg`
  - `images/class_setup.png`
  - `images/class_setup2.png`
  - `images/Rob Leaky.png`
  - `images/aed_arizona_logo.png`

## Current Status

- [x] All primary pages built and aligned to a shared design system
- [x] Global nav, footer, and cross-page linking standardized across pages
- [x] Contact + quote form layout implemented and styled to match the branded site pattern
- [x] Red banner treatment applied over the quote form header for consistency
- [x] Mobile responsiveness and stacking fixes completed
- [x] Footer copy standardized across every page
- [x] Social links corrected and navigation buttons aligned
- [x] Final copy cleanup completed, including removal of turnaround language
- [x] Site is ready for client review and deployment

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
├── README.md
├── CLIENT-UPDATES.md
├── images/
│   ├── cpr-plus-logo3.svg
│   ├── class_setup.png
│   ├── class_setup2.png
│   ├── aed_arizona_logo.png
│   ├── Rob Leaky.png
│   └── ...
└── .gitignore
```

## Notes

- The site was refined through several rounds of Figma-driven responsive and content adjustments.
- `styles.css` centralizes shared tokens, layout rules, and page-specific sections.
- Final polish included stricter mobile typography, consistent footer messaging, and cleaner contact/quote CTA hierarchy.