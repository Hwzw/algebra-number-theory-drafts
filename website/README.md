# Research website

Public site: https://hwzw.github.io/algebra-number-theory-drafts/

The repository is the content source. GitHub Actions checks out the exact pushed revision, renders every manuscript and supporting Markdown page into static HTML, and copies the PDFs without modification. Every push to `main` runs the build, validates it, and deploys the artifact to GitHub Pages. Changes become visible after that workflow succeeds; the browser does not fetch GitHub APIs or need JavaScript to read the proofs.

The homepage discovers `papers/P*/manuscript.md` automatically and links selected revisions as editions of the same paper. It does not count them as new papers. Manuscript text, disclosures, and source files remain unchanged. New manuscripts need a Markdown title, abstract, date where available, and a corresponding PDF.

Each manuscript has a canonical URL, title, description, Scholar citation metadata, direct same-directory PDF, and ScholarlyArticle structured data. A sitemap is generated at `/sitemap.xml` under the project URL. A project-level robots file cannot control the origin-root `/robots.txt`, so none is fabricated. GitHub Pages is public; search-engine inclusion remains up to each search provider. Submit the sitemap in a verified search-console property if available.

## Local checks

Requires Node.js 22 or later:

```sh
npm ci --prefix website
npm run build --prefix website
npm run check --prefix website
node website/serve.mjs
```

Preview: http://127.0.0.1:8766/algebra-number-theory-drafts/

MathJax renders math into SVG during the build; no remote fonts, scripts, analytics, or runtime APIs are required. TeX is retained as accessible labels. The build fails on formula conversion errors. Validation checks generated links and fragment identifiers, citation metadata, and byte-identical PDFs. `build-report.json` records the source commit, page counts, and formula diagnostics.

Only `website/` and `.github/workflows/pages.yml` maintain the presentation and publishing logic. `_site/` and dependencies are ignored and are never committed. The deployment workflow uses read-only repository access for building, and Pages/OIDC permissions only for publishing.
