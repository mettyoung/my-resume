# My Resume

[View my Resume](https://mettyoung.com/my-resume/dist/Young_CV.pdf)

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

Output: `dist/Young_CV.pdf`.

Custom paths: `python render.py [resume.md] [dist/Young_CV.pdf] [render.css]`

## Hooks

Git hooks live in `.githooks/` and are versioned. Enable them once per clone:

```bash
git config core.hooksPath .githooks
```

- `pre-commit` re-renders `dist/Young_CV.pdf` and stages it whenever
  `resume.md` or `render.css` changes, so the PDF never drifts out of sync.
- `post-commit` pushes `master` (this repo's default branch) to `origin`
  after every commit made on `master`.
