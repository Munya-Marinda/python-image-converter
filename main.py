from PIL import Image
import os

input_folder = 'images'
output_folder = 'converted_pngs'
os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(input_folder):
    if file_name.endswith('.png'):
        webp_path = os.path.join(input_folder, file_name)
        png_path = os.path.join(output_folder, file_name.replace('.webp', 
'.png'))

        with Image.open(webp_path) as img:
            img.save(png_path, 'PNG')
            print(f"Converted: {file_name}")

