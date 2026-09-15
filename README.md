# AZ CPR Plus+

Marketing website build for AZ CPR Plus+, implemented as a static multi-page HTML/CSS site from approved design comps.

## Project Snapshot

- Project type: static multi-page website
- Stack: HTML5 + CSS3
- Pages implemented:
  - Home: `index.html`
  - Group Training: `group-training.html`
  - Courses: `courses.html`
  - About: `about.html`
- Brand and content assets:
  - `img/cpr-plus-logo3.svg`
  - `img/class_setup.png`
  - `img/class_setup2.png`
  - `img/Rob Leaky.png`
  - `img/aed_arizona_logo.png`

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
- [x] Production canonical URLs target `https://azcprplus.com`
- [x] Sitemap, crawler rules, social metadata, and structured data added

## Production SEO Configuration

- Production origin: `https://azcprplus.com`
- Preferred hostname: apex/non-www (`azcprplus.com`)
- Production pages: `/`, `/group-training`, `/courses`, and `/about`
- The current GitHub Pages project URL is
  `https://lgprovost.github.io/AZ-CPR-Plus-/`.
- The domain is registered and its DNS is managed through GoDaddy; the website is
  deployed by GitHub Pages, not GoDaddy hosting.
- Home navigation uses `./` so it returns to the correct root on both the GitHub
  Pages project URL and the future custom domain.
- To connect the custom domain, first verify domain ownership in GitHub. Then set
  `azcprplus.com` under **Repository Settings > Pages > Custom domain**; for
  branch-based publishing, GitHub creates the repository's `CNAME` file.
- In GoDaddy DNS, point the apex records to GitHub Pages and point the `www` CNAME
  directly to `lgprovost.github.io` without the repository name. Remove the old,
  conflicting GoDaddy hosting records as part of that DNS migration.
- DNS changes can take up to 24 hours. After GitHub verifies the DNS configuration,
  enable **Enforce HTTPS** in Pages settings.
- After deployment, verify both hostnames, all four pages, and the retired home
  URLs. GitHub Pages serves static `.html` routes and does not use `web.config`.

## Local Preview

Run the site through a local server so its root-relative production links work:

```powershell
# from project root
python -m http.server 5500
```

Then open:

`http://localhost:5500/`

## Image Optimization

The pages use high-quality WebP photos with responsive `srcset` candidates. Original
PNG files remain in `img/` for future edits. Existing CSS controls image placement
and cropping; the image conversion does not crop or recolor photos. The AED logo
uses lossless compression to preserve its artwork and transparency.

Hero images load immediately with high priority. Other photos use lazy loading,
and explicit image dimensions reserve their layout space while downloading.

To regenerate the WebP assets after editing an original, run with Pillow installed:

```powershell
python scripts/optimize_images.py
```

If an original's dimensions change, also update its HTML `width`, `height`, and
`srcset` width descriptors to match the generated images.

## Client Review Workflow

Recommended process for stakeholder updates:

1. Make changes in the project files.
2. Commit with a clear message.
3. Push to `main`.
4. Share the latest commit or repository link with the client.

## Repository Structure

```text
.
├── about.html
├── group-training.html
├── courses.html
├── index.html
├── styles.css
├── README.md
├── img/
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
