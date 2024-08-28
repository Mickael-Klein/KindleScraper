import imageCropper
import pdfMaker
import screenshotter
import userInputHandler
import folderHandler
import shutil


def main():

    # Intro displayed in CMD
    userInputHandler.intro()

    # Get user input for book details and create necessary folders
    folders_path = folderHandler.create_sub_folders()
    book = userInputHandler.get_book_infos()

    # Take kindle screenshots and store in screens folder
    screenshotter_result = screenshotter.main(book["book_pages"], folders_path["screen_path"])

    if not screenshotter_result:
        print("An error occurred while screenshotting, please try again")
        return
    
    # Crop screenshots to fit Kindle's page real screen size
    image_cropper_result = imageCropper.main(folders_path["screen_path"], folders_path["cropped_path"])

    if not image_cropper_result:
        print("An error occurred while cropping images, please try again")
        return
    
    # Create PDF from cropped images
    pdfMaker_result = pdfMaker.main(folders_path["cropped_path"], folders_path["pdf_output_path"], book["book_title"])

    if not pdfMaker_result:
        print("An error occurred while creating PDF, please try again")
        return
    else:
        shutil.rmtree(folders_path["screen_path"])
        shutil.rmtree(folders_path["cropped_path"])
        print(f"PDF '{book['book_title']}.pdf' has been created successfully in '{folders_path['pdf_output_path']}'")
        print("Your Kindle book has been successfully scraped !")


if __name__ == "__main__":
    main()