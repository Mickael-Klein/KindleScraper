import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re


def main(cropped_image_folder_path, output_pdf_folder_path, output_pdf_file_name):
    try:
        # Check if cropped images folder exists
        if not os.path.exists(cropped_image_folder_path):
            raise FileNotFoundError(f"Folder: '{cropped_image_folder_path}' not found")
        print(f"Cropped images folder found: '{cropped_image_folder_path}'")
        
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_pdf_folder_path):
            os.makedirs(output_pdf_folder_path)
            print(f"Created output folder: '{output_pdf_folder_path}'")

        # List PNG files in cropped images folder
        image_files = [f for f in os.listdir(cropped_image_folder_path) if f.lower().endswith('.png')]
        if not image_files:
            raise ValueError("No PNG files found in cropped images folder")
        
        # Sort image files by their number
        def extract_number(filename):
            match = re.search(r'(\d+)', filename)
            return int(match.group(0)) if match else float('inf')

        image_files.sort(key=extract_number)
        print(f"{len(image_files)} images found")

        # Create full path for the PDF file
        if not output_pdf_file_name.lower().endswith('.pdf'):
            output_pdf_file_name += '.pdf'
        output_pdf_path = os.path.join(output_pdf_folder_path, output_pdf_file_name)

        # Create PDF file with ReportLab
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        page_width, page_height = letter  # use page dimension per point (72 per inch)
        print(f"Creating PDF file: '{output_pdf_path}'")

        for image_file in image_files:
            try:
                image_path = os.path.join(cropped_image_folder_path, image_file)
                
                # Open image with PIL
                with Image.open(image_path) as img:
                    img_width, img_height = img.size

                    # Get ratio to resize while conserving proportions
                    ratio = min(page_width / img_width, page_height / img_height)
                    new_width = img_width * ratio
                    new_height = img_height * ratio

                    # Get positions to center the image and avoid borders
                    x = (page_width - new_width) / 2
                    y = (page_height - new_height) / 2

                    # Add the image on page
                    c.drawImage(image_path, x, y, new_width, new_height)
                    print(f"'{image_file}' added to the PDF")

                    # Add new page for each image
                    c.showPage()

            except Exception as e:
                print(f"An error occurred while processing: '{image_file}': {e}")

        # Save PDF file
        c.save()
        print(f"Your PDF was successfully saved and can be found at: '{output_pdf_path}'")

    except Exception as e:
        print(f"Error: {e}")

    return True


if __name__ == "__main__":
    main()

