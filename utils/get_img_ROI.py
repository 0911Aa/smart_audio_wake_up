# -*- coding: utf-8 -*-
from PIL import Image

import settings.DIR_PATH as path





def get_ROIimg(x1=760,y1=300,x2=1280,y2=490):

    img = Image.open(path.src_path + "file.png")

    # print(img.size)

    cropped = img.crop((x1,y1,x2,y2))  # (left, upper, right, lower)

    cropped.save(path.src_path + "file1.png")



if __name__ == "__main__":

    get_ROIimg(100,240,370,485)