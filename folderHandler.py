import os
import shutil

def create_screens_folder():
    current_directory = os.getcwd()
    screens_folder_path = os.path.join(current_directory, 'Screens')
    
    if not os.path.exists(screens_folder_path):
        os.makedirs(screens_folder_path)
        return screens_folder_path
    else:
        shutil.rmtree(screens_folder_path)
        os.makedirs(screens_folder_path)
        return screens_folder_path


def create_cropped_folder():
    current_directory = os.getcwd()
    cropped_folder_path = os.path.join(current_directory, 'Cropped')

    if not os.path.exists(cropped_folder_path):
        os.makedirs(cropped_folder_path)
        return cropped_folder_path
    else:
        shutil.rmtree(cropped_folder_path)
        os.makedirs(cropped_folder_path)
        return cropped_folder_path


def create_pdf_output_folder():
    current_directory = os.getcwd()
    pdf_output_folder_path = os.path.join(current_directory, 'KindleScrapperPDF')

    if not os.path.exists(pdf_output_folder_path):
        os.makedirs(pdf_output_folder_path)
        return pdf_output_folder_path
    else:
        return pdf_output_folder_path

def create_sub_folders():
    screen_folder_path = create_screens_folder()
    cropped_folder_path = create_cropped_folder()
    pdf_output_folder_path = create_pdf_output_folder()
    
    folders_path = {
        "screen_path" : screen_folder_path,
        "cropped_path" : cropped_folder_path,
        "pdf_output_path" : pdf_output_folder_path
    }
    
    return folders_path