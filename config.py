# -*- coding: utf-8 -*-
import os

device_name="192.168.0.2:5555"
wake_time = 2.5
wait_timeout = 15
click_post_delay = 0.5
lanuch_time = 3
bundle_id = "com.taofang.iphone"
ios_device_name="86616cbaa40e52d3f9236ec982dd6f1e933a44bd"
current_path = os.path.abspath(os.path.dirname(__file__))
screenshot_folder = os.path.join(current_path,"screenshot")
if not os.path.exists(screenshot_folder):
   os.mkdir(screenshot_folder)
   print ("创建截图目录:{}".format(screenshot_folder))