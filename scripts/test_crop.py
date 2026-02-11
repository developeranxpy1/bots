from PIL import Image
import os

folder = r"C:\Users\rgb\Desktop\dnmproof"
out_folder = os.path.join(folder, "cropped_test")
if not os.path.exists(out_folder):
    os.makedirs(out_folder)

filename = "Screenshot_20251231-220258_Telegram.png"
filepath = os.path.join(folder, filename)
out_path = os.path.join(out_folder, "test_crop.png")

# Suggested crop for 1080x2412
# Top: 250px (status + header)
# Bottom: 2200px (leaving ~212px for input/nav)
# Total height: 2412. Bottom crop should be height - X.
# If we want to keep up to y=2200, then bottom = 2200.

with Image.open(filepath) as img:
    # (left, top, right, bottom)
    cropped = img.crop((0, 250, 1080, 2150))
    cropped.save(out_path)
    print(f"Saved test crop to {out_path}")
