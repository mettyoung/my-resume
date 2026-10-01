# My Resume

[View my Resume](https://mettyoung.com/my-resume/dist/Young_CV.pdf)
([latest release](https://github.com/mettyoung/my-resume/releases/latest/download/Young_CV.pdf))

Source is `resume.md`, styled via `render.css`, rendered to PDF by `render.py`.

## Build locally

```bash
# macOS deps (weasyprint needs these native libs)
brew install pango gdk-pixbuf libffi

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python render.py
```

Output: `dist/Young_CV.pdf` (gitignored — not committed).

Custom paths: `python render.py [resume.md] [dist/Young_CV.pdf] [render.css]`

## Release

`.github/workflows/release.yml` runs on every push to `master`: it renders the
PDF, attaches it to a new GitHub Release, and deploys it to GitHub Pages at
`dist/Young_CV.pdf`. The PDF is never committed, so it can't cause merge
conflicts.

## Hooks

Git hooks live in `.githooks/` and are versioned. Enable them once per clone:

```bash
git config core.hooksPath .githooks
```

- `post-commit` pushes `master` (this repo's default branch) to `origin`
  after every commit made on `master`.
