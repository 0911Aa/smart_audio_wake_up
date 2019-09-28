# -*- coding: utf-8 -*-
from utils import get_img_ROI
import cv2
import time
from skimage.measure import compare_ssim
import settings.DIR_PATH as path
from PIL import Image

def get_mic_status(driver):
    for i in range(50):
        i+=1
        driver.screenshot(path.src_path + "mic.png")
        img = Image.open(path.src_path + "mic.png")
        cropped = img.crop((100,240,370,485))
        cropped.save(path.src_path + "mic_roi.png")
        match = cv2.imread(path.src_path + "mic_match.png")
        PIC = cv2.imread(path.src_path + "mic_roi.png")
        grayA = cv2.cvtColor(PIC, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(match, cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("yuyin: {}".format(score))
        if score > 0.98:
            break

if __name__ == "__mian__":
    get_mic_status(6)