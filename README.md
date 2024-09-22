

# Image Encryption Tool 

## Overview
The **Image Encryption Tool** is a simple Python application that encrypts and decrypts images using basic pixel manipulation techniques. This tool allows users to upload an image, apply encryption through pixel-level operations, and decrypt the image to its original form.

The tool is built using **Tkinter** for the GUI and **Pillow (PIL)** for image processing. This project can be used as a basic introduction to pixel manipulation and encryption concepts.

## Features
- **Image Upload**: Users can upload `.png`, `.jpg`, or `.jpeg` image files.
- **Image Encryption**: The tool manipulates pixel values to encrypt the image.
- **Image Decryption**: Users can revert the encrypted image back to its original state.
- **Image Display**: The GUI dynamically updates to display the uploaded, encrypted, and decrypted images.
- **Simple Pixel Manipulation**: Adds or subtracts a constant value (50) to RGB pixel values for encryption and decryption.

## Requirements
To run the `image-encryption.py` tool, ensure you have the following installed:

- **Python 3.x**
- **Tkinter** (usually included with Python)
- **Pillow (PIL)** for image processing

Install the required packages using pip:
```bash
pip install pillow
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/Jibinjoseph22/image-encryption.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd image-encryption
   ```

3. Run the `image-encryption.py` file:
   ```bash
   python image-encryption.py
   ```

4. In the application:
   - Click **Upload Image** to choose an image file from your local system.
   - Click **Encrypt Image** to encrypt the image using pixel manipulation.
   - Click **Decrypt Image** to revert the encrypted image back to its original form.

## File Structure
```
image-encryption/
│
├── image-encryption.py    # Main Python script for the image encryption tool
└── README.md              # This README file
```

## Future Enhancements
- Add more advanced encryption techniques for image files.
- Implement support for batch image encryption/decryption.
- Save encrypted images in custom formats (e.g., `.enc`).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
**Jibin Joseph**  
LinkedIn: [Jibin Joseph](https://www.linkedin.com/in/jibinjoseph2)

---
