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
- The domain uses GoDaddy DNS and currently resolves to Windows/IIS hosting.
- Install and enable an SSL certificate for both `azcprplus.com` and
  `www.azcprplus.com` before deploying the included `web.config`.
- `web.config` permanently redirects HTTP and `www` requests to the preferred
  `https://azcprplus.com` hostname, redirects the retired `/home.html`, `/home`,
  and `/index.html` URLs to `/`, and serves the three extensionless page routes.
- In GoDaddy Plesk, confirm that the preferred domain is set to the non-www form
  and that the Microsoft URL Rewrite module is available. Do not add a second
  conflicting redirect in Plesk.
- After deployment, verify HTTP status and `Location` headers for both hostnames,
  all four production routes, and the retired home URLs.

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
