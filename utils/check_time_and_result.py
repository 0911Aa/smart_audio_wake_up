# -*- coding: utf-8 -*-
import time,subprocess,os
import settings.DIR_PATH as path

def check(check_time,result,case_name):
    status = True
    if check_time >= 5:
        status = False
        raise Exception("唤醒失败")
    else:
        print("\033[7;31m%s唤醒成功\033[0m"%case_name)
    if result and status:
        print("\033[7;31m%s测试通过\033[0m"%case_name)
    else:
        fail_dir_name = time.strftime("%d_%H_%M_%S")
        cmd = "adb pull sdcard/txz/log " + path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + case_name+"\\"
        print(cmd)
        os.system(cmd)
        raise Exception('测试失败')

