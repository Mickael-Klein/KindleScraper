import os
from PIL import Image
import userInputHandler

def crop_center(image, crop_width, crop_height):
    img_width, img_height = image.size

    
    left = (img_width - crop_width) // 2
    top = (img_height - crop_height) // 2
    right = (img_width + crop_width) // 2
    bottom = (img_height + crop_height) // 2

    return image.crop((left, top, right, bottom))

def crop_images_in_folder(image_folder, crop_width, crop_height, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.png')]
    
    for image_file in image_files:
        try:
            image_path = os.path.join(image_folder, image_file)
            output_path = os.path.join(output_folder, image_file)
            
            with Image.open(image_path) as img:
                
                if img.width < crop_width or img.height < crop_height:
                    print(f"The image {image_file} is too small to be cropped")
                    continue

                cropped_img = crop_center(img, crop_width, crop_height)
                cropped_img.save(output_path)
                print(f"The image {image_file} has been cropped and stored in {output_path}")

        except Exception as e:
            print(f"An error occured during processing: '{image_file}': {e}")

def main(screenshot_folder, cropped_img_folder): 
    userInputHandler.cropper_intro()

    page_dimensions_in_screenshot = userInputHandler.ask_screenshot_dimensions()

    crop_images_in_folder(screenshot_folder, page_dimensions_in_screenshot["width"], page_dimensions_in_screenshot["height"], cropped_img_folder)

    return True


if __name__ == "__main__":
    main()
