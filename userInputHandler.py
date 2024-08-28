import userInputSanitizer


def intro():
    print("Let's scrap it !")
    print("This program requires you to have pyautogui, ImageGrab, Image, ReportLab installed on your system")
    print("Please follow the instructions to get your kindle book as PDF")
    print("Make sure your Kindle desktop app is open on the first page of the book you wanna scrap")
    print("Take in consideration than a huge book is going to produce a heavy PDF, so you may consider using caliber to convert your book")
    print("This program is appropriate mainly for books which contain a considerable number of images")
    print("Which usually cause issues on convertion")
    print("Press any key when you are ready")
    input()

def cropper_intro():
    print("Now you should find a folder named Screens in the same directory than this program")
    print("You need to get the dimensions of the pages screenshotted without the unwanted borders on the sides")
    print("All the pages should have the same dimensions so you just need to get it for a single one")
    print("You can use online tools like ResizePixel to import your image and 'resize' it to get its width and height in pixel")
    print("Use any software you want, usually height will be the same as your computer screen's height")
    print("But width may vary")
    print("")

def ask_pages_number():
     while True:
        total_pages = input("Please input the total number of pages displayed (page 1 on x at the bottom) on your Kindle App:")
        
        if userInputSanitizer.is_non_negative_integer(total_pages):
            total_pages = int(total_pages)
            return total_pages
        else:
            print("Please enter a valid number of pages.")

def ask_book_title():
    while True:
        book_title = input("Please input the title of your Kindle book:")
        
        if userInputSanitizer.is_valid_string(book_title):
            return book_title.strip()
        else:
            print("Please enter a valid book title.")


def get_book_infos():
    book_title = ask_book_title()
    total_pages = ask_pages_number()
    book = {
        "book_title": book_title,
        "book_pages": total_pages
    }
    return book

def ask_screenshot_dimensions():
    while True:
        screenshot_width = input("Please input the width of the screenshot (in pixels):")
        screenshot_height = input("Please input the height of the screenshot (in pixels):")
        
        if userInputSanitizer.is_non_negative_integer(screenshot_width) and userInputSanitizer.is_non_negative_integer(screenshot_height):
            screenshot_width = int(screenshot_width)
            screenshot_height = int(screenshot_height)

            page_real_dimensions = {
                "width": screenshot_width,
                "height": screenshot_height
            }
            return page_real_dimensions
        else:
            print("Please enter valid dimensions (non-negative integers).")