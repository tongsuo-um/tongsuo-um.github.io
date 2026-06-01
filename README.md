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
    TongSuo_headshot_latest.jpg
  cv/                      # CV PDFs
    TongSuo_cv_latest.pdf
  papers/                  # publications (PDFs / preprints)
  logo_design_images/      # source images for the favicon / branding
    doing-my-best-hamster.jpg
```

## Updating the CV

The live site always links to `assets/cv/TongSuo_cv_latest.pdf`. To update:

1. (Optional, to keep an archive) Rename the existing `TongSuo_cv_latest.pdf`
   to something dated like `TongSuo_cv_20260420.pdf`.
2. Save the new version as `TongSuo_cv_latest.pdf`.
3. Commit and push. No HTML changes needed.

## Updating the headshot

The live site always loads `assets/headshot_photos/TongSuo_headshot_latest.jpg`.
Same pattern as CV — optionally archive the old one with a dated filename,
then drop the new photo in as `TongSuo_headshot_latest.jpg` and push.

## Regenerating the favicon

If you swap the source image at `assets/logo_design_images/doing-my-best-hamster.jpg`,
re-run `python make_favicon.py` to refresh `favicon.ico`, `favicon-192.png`, and
`apple-touch-icon.png`.
