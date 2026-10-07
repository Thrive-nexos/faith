# Oluwatobi Faith — personal portfolio

A complete management, storekeeping and operations portfolio built with React + TypeScript + Vite with an editorial forest-green visual identity. All personal content is in `src/content.ts`; design tokens are in `src/styles.css`. No account, database or animation package is required.

## Run and validate

Requires Node.js 22 or newer.

```sh
npm install
npm run dev
npm run lint
npm run typecheck
npm run build
npm run preview
```

The build is a static website in `dist/`. Never edit `dist/` directly.

## Vercel deployment

The full application must be pushed to GitHub, not only this README. `vercel.json` sets the framework to Vite, runs `npm ci` and `npm run build`, and serves `dist/`.

In Vercel, connect `Thrive-nexos/faith`, use `main` as the production branch and leave Root Directory at the repository root (`./`). The source files and `package.json` are at that root. A push should create a deployment when the Git integration is enabled. If needed, deploy the newest commit from Vercel; redeploying the old README-only commit will still produce a 404. Inspect build logs and confirm the deployment is Ready.

The portfolio includes the supplied CV, portrait and original certificate photographs in `public/`; these are delivered as website assets. Local reviews, PDF working output, Sites metadata, dependencies and secrets are excluded from Git. Replace the old Sites URLs in SEO metadata with your confirmed Vercel domain once available.

## Content integrity

Sources: the supplied CV, the owner's confirmation of a 2024 stockkeeping role at Olorumlami in Ogbomoso, Oyo State, and three supplied certificate photographs. Stockkeeping duties beyond the role itself remain unspecified; no inventory metrics or software proficiency are invented. NCAM dates are unspecified. Judif employment remains current “per CV” and needs owner confirmation when the CV is updated. The downloadable CV has been revised to include the confirmed storekeeping role, updated degree wording and supplied service credentials.

The original university certificate gives the qualification as Bachelor of Agricultural Technology in General Agriculture, Second Class Honours (Lower Division), dated 28 February 2024. The website uses the certificate's wording rather than the abbreviated CV wording. The NYSC certificate records service from 30 July 2025 to 29 July 2026. The Road Safety CDS certificate is dated 9 July 2026 and recognises service in Awka North, Anambra State. The documents are displayed as supplied; no external verification is implied and no invented credential IDs or verification links are added.

Certificates remain original JPEG files. CSS presentation windows hide surrounding tables/folder/letterboxing and place the document in a forest-green frame with an ivory mount. These windows do not regenerate or modify any document text, signature, seal or photograph. The dialog also links to the full original photograph. Crop rules are in `src/revision.css` and selected by each credential's `crop` field.

The refreshed studio portrait uses built-in ImageGen to improve the tiny CV image and replace its background. The original is retained at `public/images/profile/profile-main.jpg`. The edited master is `profile-studio.png`; the optimised display version is `profile-studio.webp` (about 92 KB). Because the 216 × 252 source lacks detail, the enhancement reconstructs facial detail and must be reviewed for likeness. Prompt: preserve the same man's face, glasses, hairstyle, complexion, expression and orange traditional outfit; improve sharpness and lighting; replace outdoor surroundings with a softly lit warm grey studio background; vertical editorial portrait; no text or watermark.

Experience notes are based on documented roles, not independent commissioned projects. Workspace and field photographs are illustrative and labelled. Testimonials are disabled. NYSC is now enabled because the original document was supplied. Milestones are documented career/service events, not invented awards.

## 1. Change the profile photo

Replace `public/images/profile/profile-studio.webp` with an optimised high-resolution portrait, or change `person.portrait` in `src/content.ts`. Also update its gallery entry if the path changes. The original CV photograph remains unchanged at `profile-main.jpg`. The hero crop is controlled by `.portrait-frame img` in `src/revision.css`. If using an unenhanced original portrait, update the alt text in `App.tsx` and the gallery to remove the AI-enhancement description.

## 2. Change certificate images

Place original scans in `public/images/certificates/` and update each credential's `image`. Existing images are the user's actual photographs. `crop` selects the CSS window (`degree`, `nysc` or `road-safety`). For a new straight scan, add a new crop preset to the `Credential` type and CSS, with the correct aspect ratio and an image filling 100% of its window, positioned at 0,0. Do not reuse a crop designed for a different photograph. Keep source document pixels intact.

## 3. Add a certificate

Add to `credentials` in `src/content.ts`:

```ts
{
  id: 'unique-id',
  name: 'Actual credential title',
  issuer: 'Issuing organisation',
  date: 'Actual issue date',
  image: '/images/certificates/actual-document.jpg',
  crop: 'degree', // change/add the CSS crop preset to suit the new image
  description: 'Accurate description of the credential.',
  placeholder: false
}
```

Optional `credentialId` and `verificationUrl` appear in the dialog only if supplied. Never guess verification details. Gallery layout, frame, dialog, keyboard dismissal and original-photo link are reusable.

## 4. Add a work experience

Copy an item in `experiences`, use a unique `id`, and update `dates`, `company`, `role`, `location`, `summary`, `responsibilities` and `skills`. Use `location: null` if unknown. Empty `responsibilities: []` hides the expandable detail row. Roles currently prioritise storekeeping and management for relevance. Reorder them as desired. Do not derive durations from outdated phrases in the CV: dates are the source of truth.

## 5. Add a project or case study

Add a `Project` object to `projects`. The type in `content.ts` lists every field. Copy a practice note and fill the `overview`, `problem`, `solution`, `responsibilities`, `skills`, `results` and `lessons` with verified content. These fields appear in the accessible detail dialog. Use `placeholder: true` for demonstration-only projects, and visibly label their title/description. Replace the cover in `public/images/projects/` and update `alt`. For genuine photography remove the “ILLUSTRATIVE IMAGE” label in `App.tsx` or extend each project's data with a caption flag. Extra screenshots can be added within the case-study dialog in `App.tsx`; keep their source paths in the project data. Real agriculture projects should list professional skills rather than inventing software technologies.

## 6. Add education

Add an entry to `education`: `institution`, `degree`, `field`, `graduation`, `achievement`, `image`, `alt`. The education section currently displays the original degree using the same framed-document component. To use a graduation photograph, replace that component in `App.tsx` and update the data path and caption. Store campus photographs and degree scans in this folder or the certificates folder. Update the Person structured data in `App.tsx` if the institution changes.

NYSC service details are now in `service`, with `enabled: true`. Its certificate is in the credentials gallery. Update `organisation`, `dates`, `description` to change the service story.

## 7. Change contact details

Edit `person.email` and `person.phones`. Phone values should be international numbers without spaces. All email links, phone links and email drafts update automatically. `contact.intro` controls the invitation. The form validates the name, email, subject and message, preserves entered text and prepares a `mailto:` draft. It does not send mail or store messages. Visitors must send the draft in their email application. No delivery success is claimed. To support server delivery, integrate a form provider/server endpoint, configure domain verification and abuse protection, and replace `Contact.submit` with an actual request before claiming delivery.

## 8. Change social links

The `socials` array starts empty because no accounts were provided. Add `{ label: 'LinkedIn', url: 'https://www.linkedin.com/in/your-real-profile/' }` or other confirmed accounts. Links appear in contact and structured data. Never publish guessed social profiles. Add visible footer social links in `App.tsx` if desired.

## 9. Add gallery photographs

Add files to `public/images/gallery/`. Each `gallery` object contains `src`, `alt`, `label`, `caption`, `placeholder`. Give real photos specific alt text and accurate captions; set `placeholder: false`. Workspace/field photographs are intentionally labelled illustrative; the refreshed portrait is based on the original CV portrait. The grid adapts as entries are added. Use compressed WebP/JPEGs (normally 150–300 KB) and remove sensitive information from visible certificates before public sharing.

Testimonials are configured in `testimonials`. Replace the sample with an approved quote, set `placeholder: false`, and enable the section. The sample is not published by default. Add real awards to `milestones` only with accurate titles and dates.

## 10. Change the CV

The CV has been updated to match the management/storekeeping direction and forest-green palette. The final file is `output/pdf/OJO_OLUWATOBI_FAITH_CV.pdf`; identical copies are used by the local website and static build. Edit `scripts/build_cv.py` and run it with Python + ReportLab to regenerate it, or replace `public/OJO_OLUWATOBI_FAITH_CV.pdf`. Both download links use `person.resume` in the central content. The original CV supplied by the owner remains unchanged in Downloads.

## 11. Change colours and typography

Edit the `:root` variables in `src/styles.css`; revision-specific layout and readable typography are in `src/revision.css`. Edit variables: `--forest`, `--bottle`, `--dark`, `--ivory`, `--beige`, `--gold`, `--ink`, `--muted`, `--line`. Gold is reserved for fine accents. Fonts are Cormorant Garamond and Manrope from Google Fonts with local fallback fonts. To self-host, download licensed WOFF2 files, add `@font-face`, replace the Google Fonts link in `index.html`, and keep `font-display: swap`. The imported fonts work without being bundled but need access to Google Fonts; the layout remains usable with fallbacks.

## 12. Deploy

The Sites hosting manifest is `.openai/hosting.json`. The selected Sites audience is owner-private. The current revision remains local until the owner approves uploading the portrait and certificate photographs; automatic approval review blocked the remote workflow pending that specific authorisation. Use the Sites workflow to save/deploy future edits while preserving this project ID. Making a private Site public is a separate access change.

For an alternative static host, run `npm run build` and upload `dist/`:

- Netlify: build command `npm run build`, publish directory `dist`.
- Vercel: framework Vite, build command `npm run build`, output `dist`.
- Cloudflare Pages: build command `npm run build`, output `dist`.
- Any static web server: serve `dist/` over HTTPS.

This website uses anchors and dialogs rather than route URLs, so no SPA route rewrites are required. Replace canonical/OG URLs in `index.html`, `public/robots.txt`, `public/sitemap.xml` and Person JSON-LD in `App.tsx` when using a new domain. Replace the social sharing image with an actual 1200 × 630 PNG/JPEG: some social crawlers do not support SVG. Set `og:image` to the full absolute URL of that image. The current SVG supports a preview while that raster asset is prepared.

## Accessibility and performance

Semantic sections, a skip link, native accessible modal dialogs, Escape dismissal, focus restoration, form error associations, visible focus styles, reduced-motion support, lazy loading and responsive layouts are included. Hero images load eagerly; other images load lazily. No fabricated percentage skill bars or heavy animation framework are used. Check actual Lighthouse results after deployment; no performance score is claimed without a measured report.

## Asset sources

- `profile-main.jpg`: the original portrait embedded in the user-supplied CV.
- `profile-studio.png` / `.webp`: AI-enhanced portrait, built-in ImageGen, based on the original.
- `degree-original.jpeg`, `nysc-original.jpeg`, `road-safety-service-original.jpeg`: unmodified user-supplied certificate photographs.
- `agriculture-detail.jpg`: Unsplash photo `1500382017468-9049fed747ef` (illustrative landscape).
- `project-01-cover.jpg`: Unsplash photo `1516467508483-a7212febe31a` (illustrative livestock).
- `project-02-cover.jpg`: Unsplash photo `1500937386664-56d1dfef3854` (illustrative field).
- `project-03-cover.jpg`: Unsplash photo `1455390582262-044cdead277a` (illustrative writing/workspace).
- `field-work.jpg`: Unsplash photo `1464226184884-fa280b87c399` (illustrative crops).
- SVGs: purpose-built editorial placeholders; not certificates or personal event records.

Keep a high-resolution original of every real photograph outside `public/`; put only optimised display assets in the website.

## Review files

`review/management-hero.png` and `review/framed-certificates.png` are local screenshots for reviewing the revision. They are not deployment thumbnails.
# faith
