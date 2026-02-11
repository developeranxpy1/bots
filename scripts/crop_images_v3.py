from PIL import Image
import os
import glob
from collections import Counter

def get_bg_color(img_rgb):
    w, h = img_rgb.size
    # Sample a grid in the middle
    colors = []
    for x in range(w//4, 3*w//4, 50):
        for y in range(h//4, 3*h//4, 50):
            colors.append(img_rgb.getpixel((x, y)))
    return Counter(colors).most_common(1)[0][0]

def process_images_v3(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    files = glob.glob(os.path.join(src_dir, "*.png"))
    
    for f in files:
        with Image.open(f) as img:
            img_rgb = img.convert("RGB")
            w, h = img.size
            
            # 1. Detect header end
            # We look for the first significant change from the status bar color
            # and then the first "content-like" area.
            # Usually, after the header (y~200), there's a background.
            
            # Default values for 1080x2412
            top_crop = int(320 * h / 2412) 
            bottom_crop = int(2240 * h / 2412)
            
            # Try to refine top_crop:
            # Scan from y=100 to y=500. Look for the first row that isn't mostly a solid header color.
            # But header might be multi-colored.
            # Better: Telegram header usually has a divider line.
            
            # Refine bottom_crop:
            # Scan from h-100 up. Look for the input bar.
            # The input bar is usually a distinct horizontal area.
            
            cropped = img.crop((0, top_crop, w, bottom_crop))
            out_name = os.path.basename(f)
            cropped.save(os.path.join(dest_dir, out_name))
            print(f"Processed {out_name}: top={top_crop}, bottom={bottom_crop}")

src = r"C:\Users\rgb\Desktop\dnmproof"
dest = os.path.join(src, "cropped_v3")
process_images_v3(src, dest)
