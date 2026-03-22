# Python Image WebP to PNG Converter

A simple Python script to convert `.webp` images to `.png` format.

## Project Structure

```

python-image-webp-to-png/
├── images/ # Place your .webp images here
├── converted_pngs/ # Converted .png images will be saved here
├── main.py # Main script
└── requirements.txt # Python dependencies

```

## Setup

1. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python main.py
```

All `.webp` images in the `images/` folder will be converted to `.png` and saved in `converted_pngs/`.

## Dependencies

- [Pillow](https://pypi.org/project/Pillow/) – for image conversion

## Notes

- Make sure the `images/` folder contains `.webp` files before running the script.
- The script preserves the original filenames but changes the extension to `.png`.

```bash
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```
