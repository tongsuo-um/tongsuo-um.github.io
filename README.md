# tongsuo-um.github.io

Personal academic website for Tong Suo, served at <https://tongsuo-um.github.io>.

Plain static HTML/CSS — no build step. To preview locally, open `index.html` in a browser.

## Folder layout

```
index.html
style.css
make_favicon.py            # regenerates the favicon from the source hamster image
assets/
  favicon.ico              # site favicon (referenced from index.html)
  favicon-192.png
  apple-touch-icon.png
  headshot_photos/         # profile photos
    headshot.jpg
  cv/                      # CV PDFs
    Tong_Suo_CV.pdf
  papers/                  # publications (PDFs / preprints)
  logo_design_images/      # source images for the favicon / branding
    doing-my-best-hamster.jpg
```

## Updating the CV

Replace `assets/cv/Tong_Suo_CV.pdf` with the new PDF (keep the same filename) and push.

## Updating the headshot

Replace `assets/headshot_photos/headshot.jpg` (keep the same filename) and push.

## Regenerating the favicon

If you swap the source image at `assets/logo_design_images/doing-my-best-hamster.jpg`,
re-run `python make_favicon.py` to refresh `favicon.ico`, `favicon-192.png`, and
`apple-touch-icon.png`.
