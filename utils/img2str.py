# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import settings.DIR_PATH as path

def get_str():
    pytesseract.pytesseract.tesseract_cmd = 'D://Program Files (x86)/Tesseract-OCR/tesseract.exe'
    img = Image.open(path.src_path+'file1.png')
    text = pytesseract.image_to_string(img,lang='eng')
    try:
        if " " in text:
            return text.split()[0]
        return text.split('.')[0]+'.'+text.split('.')[1]
    except:
        return "0"

if __name__ == "__main__":
    print(get_str())