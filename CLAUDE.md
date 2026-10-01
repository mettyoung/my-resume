# Repo conventions

- This repo's default branch is `master` (there is no `main`). Work directly
  on `master`. Commit and push straight to `origin/master` — do not create
  feature branches for changes in this repo.
- `resume.md` is the source of truth for the resume. `dist/Young_CV.pdf` is a
  build output and is gitignored — never commit it. CI
  (`.github/workflows/release.yml`) renders it on every push to `master`,
  publishes it as a GitHub Release asset, and deploys it to GitHub Pages.
- Hooks are versioned in `.githooks/` (enable once per clone with
  `git config core.hooksPath .githooks`):
  - `post-commit` pushes `master` to `origin` after every commit made on
    `master`.
