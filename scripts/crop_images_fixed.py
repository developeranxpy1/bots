from PIL import Image
import os
import glob

def process_images_fixed(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    files = glob.glob(os.path.join(src_dir, "*.png"))
    
    # Standard crop for 1080x2412 Telegram screenshots
    top_px = 280
    bottom_px = 2150 # Height until which to keep (so crops from 2150 to 2412)
    
    for f in files:
        with Image.open(f) as img:
            w, h = img.size
            # Adjust if different resolution, but these are likely all the same
            # Scale proportionally if needed
            t = int(top_px * h / 2412)
            b = int(bottom_px * h / 2412)
            
            cropped = img.crop((0, t, w, b))
            out_name = os.path.basename(f)
            cropped.save(os.path.join(dest_dir, out_name))
            print(f"Processed {out_name} with fixed crop.")

src = r"C:\Users\rgb\Desktop\dnmproof"
dest = os.path.join(src, "cropped_v2")
process_images_fixed(src, dest)
