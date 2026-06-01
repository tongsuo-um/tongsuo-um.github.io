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
    TongSuo_headshot_2021Aug.jpg
  cv/                      # CV PDFs
    TongSuo_cv_20260420.pdf
  papers/                  # publications (PDFs / preprints)
  logo_design_images/      # source images for the favicon / branding
    doing-my-best-hamster.jpg
```

## Updating the CV

Drop the new CV PDF into `assets/cv/` (filenames are dated, e.g.
`TongSuo_cv_YYYYMMDD.pdf`, so older versions are preserved). Then update the
`href` in `index.html` (search for `cv/TongSuo_cv_`) to point at the new file
and push.

## Updating the headshot

Drop the new photo into `assets/headshot_photos/` (filenames are dated, e.g.
`TongSuo_headshot_YYYYMon.jpg`). Then update the `src` in `index.html`
(search for `headshot_photos/TongSuo_headshot_`) to point at the new file
and push.

## Regenerating the favicon

If you swap the source image at `assets/logo_design_images/doing-my-best-hamster.jpg`,
re-run `python make_favicon.py` to refresh `favicon.ico`, `favicon-192.png`, and
`apple-touch-icon.png`.
