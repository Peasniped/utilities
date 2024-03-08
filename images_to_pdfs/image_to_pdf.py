# Adapted from https://www.geeksforgeeks.org/python-convert-image-to-pdf-using-img2pdf-module/

import img2pdf
from PIL import Image
import os

def rename_pngs_to_jpgs(img_folder_path:str):
    all_files = os.listdir(img_folder_path)
    jpgs = [file.lower() for file in all_files if ".jpg" in file or ".jpeg" in file]

    if jpgs == []:
        print(f"No files with extensions '.jpg' or '.jpeg' in folder {img_folder_path}\n")

    for jpg in jpgs:
        old_filename = img_folder_path + "\\" + jpg
        new_filename = img_folder_path + "\\" + jpg[:-4] + ".png" if ".jpg" in jpg else img_folder_path + "\\" + jpg[:-5] + ".png"

        os.rename(old_filename, new_filename)
        print(f"File '{old_filename}' has successfully been renamed to '{new_filename}'")

def convert_pngs_to_pdfs(img_folder_path:str, pdf_folder_path:str):
    all_files = os.listdir(img_folder_path)
    files = [file.lower for file in all_files if ".png" in file]

    for file in files:
        img_path = img_folder_path + "\\" + file
        pdf_path = pdf_folder_path + "\\" + file[:-4] + ".pdf"
        
        image = Image.open(img_path)
        pdf_bytes = img2pdf.convert(image.filename)
        
        file = open(pdf_path, "wb")
        file.write(pdf_bytes)
        
        image.close()
        file.close()
        
        print(f"Successfully converted {img_path} to {pdf_path}")

if __name__ == "__main__":
    img_folder_path = "C:\images_to_pdfs\images"
    pdf_folder_path = "C:\images_to_pdfs\pdfs"

    rename_pngs_to_jpgs(img_folder_path)
    convert_pngs_to_pdfs(img_folder_path, pdf_folder_path)
