"""Generate square-cropped variants of the headshot for high-DPI / home-screen use.

The CSS hero uses object-position: center 20% (anchored toward the top so the
top of the head isn't clipped). This script does the equivalent crop in the
source file: take a square slice from the original, biased upward, then
downscale to common icon sizes.
"""
from PIL import Image
import os

SRC = os.path.join(
    os.path.dirname(__file__), "assets", "headshot_photos", "TongSuo_headshot_latest.jpg"
)
OUT_DIR = os.path.join(os.path.dirname(__file__), "assets", "headshot_photos")

img = Image.open(SRC).convert("RGB")
w, h = img.size
side = min(w, h)
x0 = (w - side) // 2
y0 = int((h - side) * 0.20)
square = img.crop((x0, y0, x0 + side, y0 + side))

square.resize((192, 192), Image.LANCZOS).save(
    os.path.join(OUT_DIR, "TongSuo_headshot_latest_android_192.png")
)
square.resize((180, 180), Image.LANCZOS).save(
    os.path.join(OUT_DIR, "TongSuo_headshot_latest_apple_touch_180.png")
)

print(f"Source: {w}x{h}, square crop: {side}x{side} from ({x0},{y0})")
print(f"Wrote TongSuo_headshot_latest_android_192.png and TongSuo_headshot_latest_apple_touch_180.png")
