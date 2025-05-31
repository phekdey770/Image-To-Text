import os
from PIL import Image
import pytesseract

# Path to the folder containing images
folder_path = r"C:\Code Workpace\VS Code\Python 3\Z - Other\Data\Quote"

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert_images_to_text(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            # Construct full file path
            image_path = os.path.join(folder_path, filename)
            
            # Open the image
            img = Image.open(image_path)
            
            # Convert image to text
            text = pytesseract.image_to_string(img)
            
            # Create a text file name based on the image file name
            text_file_name = os.path.splitext(filename)[0] + '.txt'
            text_file_path = os.path.join(folder_path, text_file_name)
            
            # Save the extracted text to a text file
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)
            
            print(f"Text extracted from {filename} and saved to {text_file_name}")

# Run the function to convert images to text
convert_images_to_text(folder_path)
