# -*- coding: utf-8 -*-
import os
import cv2
import time
from skimage.measure import compare_ssim
import settings.DIR_PATH as path

def picture_match(driver,img_list,sco=0.8):
    tm = time.strftime("%Y%m%d_%H%M%S")
    driver.screenshot("file.png")
    match = cv2.imread('file.png')
    for img in  img_list:
        PIC = cv2.imread(path.img_path+img)
        grayA = cv2.cvtColor(PIC, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(match, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))

        if score > sco:
            # os.rename(os.path.join(os.getcwd(), '01.png'), os.path.join(path, tm + str(row) + ".png"))
            return score
    return None