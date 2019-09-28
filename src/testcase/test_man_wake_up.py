# -*- coding: utf-8 -*-
'''
Created on 2018年11月20日

@author: uidq1501
'''

from utils.play_aidio import play
from utils.record_audio import get_audio
import pyaudio
import threading
import os
import settings.DIR_PATH as path
import pytest,time,allure
from utils.driver import Driver
from config import *
from utils import get_device_log as gdl

@allure.feature("男生唤醒测试")
@pytest.mark.P1
class Test_wake:
    def setup_class(cls):

        dr = Driver()

        cls.driver = dr.init_driver(device_name)

        cls.GDL = gdl.Get_device_log()



    def teardown(self):
        cmd = 'del /F /S /Q D:\\text_all_new'

        os.system(cmd)

    @allure.story('0001.男生唤醒')
    @pytest.mark.repeat(5)
    def test_case1(self):
        GDL = gdl.Get_device_log()  # 初始化

        play('woman_wake_up', path.wake_up_file)  # 播放唤醒词
        wake_finish_time = GDL.get_local_time()
        print(wake_finish_time)
        time.sleep(2)
        self.driver.screenshot(path.Cache_img_path2)
        time.sleep(28)
        GDL.get_device_log()
        time.sleep(1)
        start_time = GDL.get_begin_parse()
        print("\033[7;31m收到唤醒词的时间：\033[0m", start_time)
        end_time, new_result = GDL.get_device_wake()
        print("返回%s的时间是%f" % (new_result, end_time))
        wait_time = end_time - start_time
        check_time = abs(wake_finish_time - start_time)
        print("唤醒耗时", wait_time)
        print("本地时间误差", check_time)
        if wait_time >= 2 or check_time >= 5:
            fail_dir_name = time.strftime("%d_%H_%M_%S")
            cmd = "adb pull sdcard/txz/log " + path.DIR_PATH + "\\report\\error_log\\" + fail_dir_name + "women_wake_up\\"
            print(cmd)
            os.system(cmd)
            raise Exception("唤醒异常")

