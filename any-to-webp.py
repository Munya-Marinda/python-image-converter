from PIL import Image
import os

input_folder = 'images'
output_folder = 'converted_webp'
os.makedirs(output_folder, exist_ok=True)

supported_formats = ('.webp', '.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(supported_formats):
        input_path = os.path.join(input_folder, file_name)
        webp_path = os.path.join(output_folder, file_name.replace(os.path.splitext(file_name)[1], '.webp'))

        with Image.open(input_path) as img:
            img.save(webp_path, 'WEBP')
            print(f"Converted: {file_name} → {webp_path}")