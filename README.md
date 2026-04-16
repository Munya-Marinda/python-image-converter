# Python Image Converter (WEBP & PNG)

Batch image conversion scripts using Pillow.

Supports converting common image formats into:

- **WEBP** (for compression / web usage)
- **PNG** (for compatibility / transparency)

---

## Features

- Batch processing from a single folder
- Supports multiple input formats
- Converts to:
  - `.webp`
  - `.png`

- Preserves filenames
- Handles transparency (PNG conversion)

---

## Project Structure

```id="4s0fpt"
.
├── any-to-png.py        # Convert images → PNG
├── any-to-webp.py       # Convert images → WEBP
├── images               # Input images
├── converted_png        # PNG output
├── converted_webp       # WEBP output
├── requirements.txt
```

---

## Installation

### 1. Create virtual environment

```bash id="9s9j3q"
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash id="9s2bdz"
pip install -r requirements.txt
```

---

## Usage

### Convert to WEBP

```bash id="h7j9n8"
python any-to-webp.py
```

Output:

```id="ahk0t2"
converted_webp/
```

---

### Convert to PNG

```bash id="wq7v6m"
python any-to-png.py
```

Output:

```id="w2x9np"
converted_png/
```

---

## Supported Input Formats

```id="b7v3pn"
.webp, .jpg, .jpeg, .bmp, .tiff
```

---

## How It Works

### WEBP conversion

- Reads images from `images/`
- Converts and saves as `.webp`
- Useful for reducing file size for web

---

### PNG conversion

- Converts images to RGBA
- Ensures transparency support
- Outputs `.png` format

---

## Notes

- Existing files are overwritten (can be modified to skip)
- WEBP conversion does not set compression quality (can be adjusted)
- PNG files are typically larger than WEBP

---

## Optional Improvements

- Add quality control for WEBP:

```python id="p3w0md"
img.save(webp_path, 'WEBP', quality=80)
```

- Skip existing files
- Add CLI arguments (input/output folders)
- Merge both scripts into one tool

---

## Example

| Input    | Output                     |
| -------- | -------------------------- |
| JPG/PNG  | WEBP (smaller size)        |
| WEBP/JPG | PNG (better compatibility) |

---

## License

MIT
