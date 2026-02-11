from PIL import Image
import os

def find_crop_points(img_path):
    with Image.open(img_path) as img:
        img = img.convert("RGB")
        width, height = img.size
        
        # Sample the top-left color as the header color
        header_color = img.getpixel((0, 0))
        
        # Sample center column
        mid_x = width // 2
        
        top_crop = 0
        for y in range(height // 2):
            p = img.getpixel((mid_x, y))
            # If color differs significantly from header color, we might be in the chat
            # (using a threshold)
            diff = sum(abs(p[i] - header_color[i]) for i in range(3))
            if diff > 60: # Threshold for deviation
                top_crop = y
                break
        
        # Footer detection: start from bottom
        # Bottom navigation/input usually has a different color or complex patterns
        footer_color = img.getpixel((mid_x, height - 1))
        bottom_crop = height
        for y in range(height - 1, height // 2, -1):
            p = img.getpixel((mid_x, y))
            diff = sum(abs(p[i] - footer_color[i]) for i in range(3))
            if diff > 60:
                bottom_crop = y
                break
                
        return top_crop, bottom_crop

folder = r"C:\Users\rgb\Desktop\dnmproof"
filename = "Screenshot_20251231-220258_Telegram.png"
filepath = os.path.join(folder, filename)
tc, bc = find_crop_points(filepath)
print(f"Detected Crop: top={tc}, bottom={bc}")
