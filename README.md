# tongsuo-um.github.io

Personal academic website for Tong Suo, served at <https://tongsuo-um.github.io>.

Plain static HTML/CSS — no build step. To preview locally, open `index.html` in a browser.

## Folder layout

```
index.html
style.css
make_favicon.py                # regenerates the hamster favicons from the source image
make_headshot_variants.py      # regenerates the square-cropped headshot variants
assets/
  headshot_photos/             # profile photos
    TongSuo_headshot_latest.jpg                       # source, used by the hero <img>
    TongSuo_headshot_latest_android_192.png           # 192x192 square crop (Android home-screen size)
    TongSuo_headshot_latest_apple_touch_180.png       # 180x180 square crop (iOS home-screen size)
  cv/                          # CV PDFs
    TongSuo_cv_latest.pdf
  papers/                      # publications (PDFs / preprints)
  logo_design_images/          # branding / favicons (referenced from index.html)
    doing-my-best-hamster.jpg  # source image for the favicons
    hamster_tab_logo.ico       # browser-tab favicon
    hamster_android_192.png    # 192x192 PNG (Android home-screen)
    hamster_apple_touch_180.png # 180x180 PNG (iOS home-screen)
```

Currently the home-screen icon (what shows when someone saves the site to their
phone) is the **hamster**. The headshot variants are pre-generated so you can
swap the home-screen icon to your face later if you change your mind — just
re-point the `<link rel="icon" sizes="192x192">` and `<link rel="apple-touch-icon">`
tags in `index.html` at the `headshot_photos/` versions.

## Updating the CV

The live site always links to `assets/cv/TongSuo_cv_latest.pdf`. To update:

1. (Optional, to keep an archive) Rename the existing `TongSuo_cv_latest.pdf`
   to something dated like `TongSuo_cv_20260420.pdf`.
2. Save the new version as `TongSuo_cv_latest.pdf`.
3. Commit and push. No HTML changes needed.

## Updating the headshot

The live site always loads `assets/headshot_photos/TongSuo_headshot_latest.jpg`.
Same pattern as CV — optionally archive the old one with a dated filename,
then drop the new photo in as `TongSuo_headshot_latest.jpg`. After replacing
the source, run `python make_headshot_variants.py` to refresh the 192/180
square crops, then push.

## Regenerating the favicons

If you swap the source image at `assets/logo_design_images/doing-my-best-hamster.jpg`,
re-run `python make_favicon.py` to refresh the `.ico`, the 192 PNG, and the
180 apple-touch PNG inside `assets/logo_design_images/`.
