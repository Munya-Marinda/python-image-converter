from PIL import Image
import os

input_folder = 'images'
output_folder = 'converted_png'
os.makedirs(output_folder, exist_ok=True)

supported_formats = ('.webp', '.jpg', '.jpeg', '.bmp', '.tiff')

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, file_name)

        # force .png output name
        base_name = os.path.splitext(file_name)[0]
        output_path = os.path.join(output_folder, base_name + '.png')

        with Image.open(input_path) as img:
            # ensure compatibility (important for WEBP transparency, etc.)
            img = img.convert("RGBA")
            img.save(output_path, 'PNG')

        print(f"Converted: {file_name} → {output_path}")