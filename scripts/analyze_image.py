from PIL import Image
import os

folder = r"C:\Users\rgb\Desktop\dnmproof"
filename = "Screenshot_20251231-220258_Telegram.png"
filepath = os.path.join(folder, filename)

with Image.open(filepath) as img:
    width, height = img.size
    print(f"Dimensions: {width}x{height}")
    
    # Sample center vertical line to find color changes
    mid_x = width // 2
    pixels = [img.getpixel((mid_x, y)) for y in range(height)]
    
    # Print first and last 500 pixels (roughly) to see where the color stabilizes or changes
    # We'll look for the transition from the header color to the chat background
    print("Top 300 pixels colors:")
    for y in range(0, 300, 10):
        print(f"y={y}: {pixels[y]}")
        
    print("\nBottom 300 pixels colors:")
    for y in range(height-300, height, 10):
        print(f"y={y}: {pixels[y]}")
