from PIL import Image
import os
import glob

def process_images(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    files = glob.glob(os.path.join(src_dir, "*.png"))
    
    for f in files:
        with Image.open(f) as img:
            img_rgb = img.convert("RGB")
            w, h = img.size
            
            # Heuristic for 1080x2412 Telegram screenshots
            # Top header is usually consistent
            # We'll scan from top for the first significant change across the middle section
            
            top_crop = 0
            header_color = img_rgb.getpixel((w//2, 10)) # Sample header color
            for y in range(10, h // 3):
                p = img_rgb.getpixel((w//2, y))
                diff = sum(abs(p[i] - header_color[i]) for i in range(3))
                if diff > 30: # Found start of chat area or divider
                    top_crop = y
                    break
            
            # Add a bit of padding to avoid the header shadow/line
            top_crop += 20 

            # Bottom: Input bar + Navigation
            # We'll scan from bottom for the first significant change
            bottom_crop = h
            footer_color = img_rgb.getpixel((w//2, h - 10))
            for y in range(h - 10, h // 2, -1):
                p = img_rgb.getpixel((w//2, y))
                diff = sum(abs(p[i] - footer_color[i]) for i in range(3))
                if diff > 30: # Found end of chat area (input bar)
                    bottom_crop = y
                    break
            
            # Back off a bit from the input bar
            bottom_crop -= 10
            
            if top_crop >= bottom_crop:
                # Fallback to defaults if detection fails
                top_crop = 260
                bottom_crop = h - 250
            
            cropped = img.crop((0, top_crop, w, bottom_crop))
            out_name = os.path.basename(f)
            cropped.save(os.path.join(dest_dir, out_name))
            print(f"Processed {out_name}: top={top_crop}, bottom={bottom_crop}")

src = r"C:\Users\rgb\Desktop\dnmproof"
dest = os.path.join(src, "cropped")
process_images(src, dest)
