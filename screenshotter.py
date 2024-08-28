import pyautogui
import time
from PIL import ImageGrab

def go_fullscreen():
    pyautogui.press('f11')

def exit_fullscreen():
    pyautogui.press('f11')

def turn_page():
    pyautogui.press('right')

def take_screenshot(page_number, screens_folder_path):
    screenshot = ImageGrab.grab()
    screenshot.save(f'{screens_folder_path}/page_{page_number}.png')

def main(pages_number, screens_folder_path):

    print("After pressing a key, open the kindle desktop app window with your book already opened on page 1 and wait for the program to finish the whole book, then go back to this terminal to next step")
    print("Remember to move your mouse on the outside of the kindle book page to not have it on your pdf ^^")
    print("you will have 8 seconds to do so")
    input("press any key to start...")

    time.sleep(8)
    
    go_fullscreen()
    time.sleep(5)
    
    
    for page_number in range(1, pages_number + 1):
        take_screenshot(page_number, screens_folder_path)
        print(f"Page {page_number} screenshotted")
        turn_page()
        time.sleep(2)

    exit_fullscreen()
    print("All pages has been screenshotted")
    return True

if __name__ == "__main__":
    main()