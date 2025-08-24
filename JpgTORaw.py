import sys
from PIL import Image
import struct
import os

def convert_to_rgb565(input_path, output_path):
    # Open and convert the image
    image = Image.open(input_path).convert('RGB')
    image = image.resize((480, 320))  # Resize to match ILI9488 resolution

    # Write as .raw in RGB565 (big-endian)
    with open(output_path, 'wb') as f:
        for y in range(320):
            for x in range(480):
                r, g, b = image.getpixel((x, y))
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                f.write(struct.pack('>H', rgb565))  # >H = big-endian unsigned short

    print(f"✅ Converted '{input_path}' → '{output_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Usage: python convert_image_to_raw.py <input_image> <output_raw>")
        print("Example: python convert_image_to_raw.py monday.jpg 1.raw")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"❌ Input file '{input_file}' not found.")
        sys.exit(1)

    convert_to_rgb565(input_file, output_file)
