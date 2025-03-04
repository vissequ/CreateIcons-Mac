#!/usr/bin/env python3
import os
from PIL import Image

def create_iconset(input_png, output_dir="icon.iconset"):
    """
    Takes a PNG file and generates multiple sizes for a macOS .icns file.
    Saves the resized images into an 'icon.iconset' folder.
    
    Args:
        input_png (str): Path to the input PNG file.
        output_dir (str): Directory to save the iconset (default: 'icon.iconset').
    """
    # Define the required sizes for macOS .icns
    icon_sizes = [
        (16, "icon_16x16.png"),       # 16x16
        (32, "icon_16x16@2x.png"),   # 32x32 (Retina for 16x16)
        (32, "icon_32x32.png"),       # 32x32
        (64, "icon_32x32@2x.png"),   # 64x64 (Retina for 32x32)
        (128, "icon_128x128.png"),    # 128x128
        (256, "icon_128x128@2x.png"),# 256x256 (Retina for 128x128)
        (256, "icon_256x256.png"),    # 256x256
        (512, "icon_256x256@2x.png"),# 512x512 (Retina for 256x256)
        (512, "icon_512x512.png"),    # 512x512
        (1024, "icon_512x512@2x.png"),# 1024x1024 (Retina for 512x512)
    ]

    # Open the input image
    try:
        with Image.open(input_png) as img:
            # Ensure the image is in RGBA mode (for transparency)
            if img.mode != "RGBA":
                img = img.convert("RGBA")

            # Create the output directory if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)

            # Resize and save each icon size
            for size, filename in icon_sizes:
                resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
                output_path = os.path.join(output_dir, filename)
                resized_img.save(output_path, "PNG")
                print(f"Saved: {output_path}")

            print(f"\nIconset created in '{output_dir}'.")
            print("To convert to .icns, run: 'iconutil -c icns icon.iconset'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_png}' not found.")
    except Exception as e:
        print(f"Error processing image: {e}")

def find_png_in_root():
    """
    Searches the script's root directory for a .png file and returns the first one found.
    Returns None if no .png file is found.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script's directory
    for filename in os.listdir(script_dir):
        if filename.lower().endswith(".png"):
            return os.path.join(script_dir, filename)
    return None

def main():
    # Find a PNG file in the script's root directory
    input_png = find_png_in_root()
    
    if input_png:
        print(f"Found PNG file: {input_png}")
        create_iconset(input_png)
    else:
        print("Error: No .png file found in the script's root directory.")
        print("Place a .png file in the same directory as this script and try again.")

if __name__ == "__main__":
    main()
