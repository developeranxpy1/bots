from PIL import Image
import os

folder = r"C:\Users\rgb\Desktop\dnmproof"
filename = "Screenshot_20251231-220258_Telegram.png"
filepath = os.path.join(folder, filename)

with Image.open(filepath) as img:
    img = img.convert("RGB")
    width, height = img.size
    
    # Analyze the center column more densely
    mid_x = width // 2
    for y in range(0, height, 20):
        p = img.getpixel((mid_x, y))
        # Also check a bit to the left and right to avoid text
        p_left = img.getpixel((mid_x - 100, y))
        p_right = img.getpixel((mid_x + 100, y))
        print(f"y={y:4}: C={p} L={p_left} R={p_right}")
