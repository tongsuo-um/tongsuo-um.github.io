"""One-off script to turn the hamster sticker into a circular favicon."""
from PIL import Image, ImageDraw
import os

SRC = os.path.join(os.path.dirname(__file__), "assets", "logo_design_images", "doing-my-best-hamster.jpg")
OUT_DIR = os.path.join(os.path.dirname(__file__), "assets")

img = Image.open(SRC).convert("RGBA")
w, h = img.size

def is_white(px, tol=15):
    r, g, b, a = px
    return a > 0 and r > 255 - tol and g > 255 - tol and b > 255 - tol

px = img.load()
non_white_xs, non_white_ys = [], []
step = 4
for y in range(0, h, step):
    for x in range(0, w, step):
        if not is_white(px[x, y]):
            non_white_xs.append(x)
            non_white_ys.append(y)

x0, x1 = min(non_white_xs), max(non_white_xs)
y0, y1 = min(non_white_ys), max(non_white_ys)
cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
half = max(x1 - x0, y1 - y0) // 2
pad = int(half * 0.04)
half -= pad
square = img.crop((cx - half, cy - half, cx + half, cy + half))

size = square.size[0]
mask = Image.new("L", (size, size), 0)
inset = int(size * 0.075)
ImageDraw.Draw(mask).ellipse((inset, inset, size - inset, size - inset), fill=255)
masked = Image.new("RGBA", (size, size), (0, 0, 0, 0))
masked.paste(square, (0, 0), mask)

large = masked.resize((512, 512), Image.LANCZOS)
masked.resize((192, 192), Image.LANCZOS).save(os.path.join(OUT_DIR, "favicon-192.png"))
masked.resize((180, 180), Image.LANCZOS).save(os.path.join(OUT_DIR, "apple-touch-icon.png"))

ico_sizes = [(16, 16), (32, 32), (48, 48)]
large.save(
    os.path.join(OUT_DIR, "favicon.ico"),
    format="ICO",
    sizes=ico_sizes,
)

print(f"Cropped square: {size}x{size}")
print(f"Wrote favicon.ico (sizes {ico_sizes}), favicon-192.png, apple-touch-icon.png")
