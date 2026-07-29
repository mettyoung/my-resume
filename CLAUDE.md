# Repo conventions

- This repo's default branch is `master` (there is no `main`). Work directly
  on `master`. Commit and push straight to `origin/master` — do not create
  feature branches for changes in this repo.
- `resume.md` is the source of truth for the resume; `dist/Young_CV.pdf` is
  the rendered, committed artifact and must stay in sync with it.
- Hooks are versioned in `.githooks/` (enable once per clone with
  `git config core.hooksPath .githooks`):
  - `pre-commit` re-runs `render.py` and stages `dist/Young_CV.pdf` whenever
    `resume.md` or `render.css` is part of the commit.
  - `post-commit` pushes `master` to `origin` after every commit made on
    `master`.
