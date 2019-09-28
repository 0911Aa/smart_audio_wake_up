# -*- coding: utf-8 -*-
import time,os
import settings.DIR_PATH as path

# fail_dir_name = time.strftime("%y_%m_%d_%H_%M_%S")
# print(fail_dir_name)

men_question_list = os.listdir(path.men_question_file)
for i in men_question_list:
    file_name = i.split(".")[0]
