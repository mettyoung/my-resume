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
