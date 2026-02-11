from PIL import Image
import os
import glob

def strip_all_metadata(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    files = glob.glob(os.path.join(src_dir, "*.png"))
    
    for f in files:
        out_name = os.path.basename(f)
        dest_path = os.path.join(dest_dir, out_name)
        
        with Image.open(f) as img:
            # Create a fresh image using only the pixel data
            # This strips all EXIF, ICC profiles, and other metadata
            data = list(img.getdata())
            stripped = Image.new(img.mode, img.size)
            stripped.putdata(data)
            
            # Save without any extra info
            stripped.save(dest_path, "PNG", optimize=True)
            print(f"Stripped metadata from {out_name}")

src = r"C:\Users\rgb\Desktop\dnmproof\cropped_v3"
dest = r"C:\Users\rgb\Desktop\dnmproof\cropped_v3_stripped"
strip_all_metadata(src, dest)
