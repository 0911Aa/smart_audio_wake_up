# -*- coding: utf-8 -*-
"""
@ Description：Pytest hook Appium

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址
# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # 用例报错捕捉
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         f = Action.driver.get_screenshot_as_png()
#         allure.attach(f, '失败截图', allure.attachment_type.PNG)
#         logcat = Action.driver.get_log('logcat')
#         c = '\n'.join([i['message'] for i in logcat])
#         allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
        # if Action.get_app_pid() != Action.apppid:
        #     raise Exception('设备进程 ID 变化，可能发生崩溃')

import os,sys,subprocess,pytest,time,allure
import base64,atx
# from android.module.base import Base
import uiautomator2 as ut2
import uiautomator2.ext.htmlreport as htmlreport
from utils.driver import Driver
from config import *
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
import settings.DIR_PATH as path
sys.path.append('..')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 用例报错捕捉
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            # f = adb_screen_shot()
            # f1 = open(path.Cache_img_path1, 'rb').read()
            f2 = open(path.Cache_img_path2, 'rb').read()
            # allure.attach(f1, '失败截图', allure.attachment_type.PNG)
            allure.attach(f2, '失败截图', allure.attachment_type.PNG)
            cb = open(path.log_path,'rb').read()
            c = cb.decode("utf-8","ignore")
            allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
        except Exception as e:
            print(e,"截图或log抓取失败")

# 当设置autouse为True时,
# 在一个session内的所有的test都会自动调用这个fixture
# @pytest.fixture()
# def driver_setup(request):
#     print("自动化测试开始!")
#     request.instance.driver = Driver().init_driver(device_name)
#     print("driver初始化")
#     time.sleep(lanuch_time)
#     allow(request.instance.driver)
#     def driver_teardown():
#         print("自动化测试结束!")
#     request.addfinalizer(driver_teardown)


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''
#     hook pytest失败
#     :param item:
#     :param call:
#     :return:
#     '''
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         pic_info = adb_screen_shot()
#         with allure.step('添加失败截图...'):
#             allure.attach("失败截图", pic_info, allure.attachment_type.PNG)


def allow(driver):
    driver.watcher("允许").when(text="允许").click(text="允许")
    driver.watcher("跳过 >").when(text="跳过 >").click(text="跳过 >")
    driver.watcher("不要啦").when(text="不要啦").click(text="不要啦")


def screen_shot(driver):
    '''
    截图操作
    pic_name:截图名称
    :return:
    '''
    try:
        fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        fail_pic = str(fail_time) + "截图"
        pic_name = os.path.join(screenshot_folder, fail_pic)
        driver.screenshot("{}.jpg".format(pic_name))
        print('截图:{}'.format(pic_name))
        f = open(pic_name, 'rb')  # 二进制方式打开图文件
        base64_str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return base64_str
    except Exception as e:
        print("{}截图失败!{}".format(pic_name, e))


def adb_screen_shot():
    '''
    adb截图
    :return:
    '''
    file_info = ''
    fail_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fail_pic = str(fail_time) + "截图.jpg"
    pic_name = os.path.join(screenshot_folder, fail_pic)
    cmd = 'adb shell /system/bin/screencap -p /sdcard/screenshot.jpg'
    subprocess.call(cmd,shell=True)
    cmd = 'adb pull /sdcard/screenshot.jpg {}'.format(pic_name)
    subprocess.call(cmd, shell=True)
    with open(pic_name, 'rb') as r:
        file_info = r.read()
    return file_info



# 当设置autouse为True时,
# 在一个session内的所有的test都会自动调用这个fixture
# @pytest.fixture(autouse=True)
# def ios_driver_setup(request):
#     logger.info("ios自动化测试开始!")
#     request.instance.driver = Driver().init_ios_driver(ios_device_name)
#     logger.info("driver初始化")
#     ios_allow(request.instance.driver)
#     def driver_teardown():
#         logger.info("ios自动化测试结束!")
#         request.instance.driver.stop_app()
#     request.addfinalizer(driver_teardown)


# def ios_allow(driver):
#     elem = driver(name="允许")
#     if elem.exists:
#        elem.click()
#     if elem.exists:
#        elem.click()
#     elem = driver(xpath='//XCUIElementTypeButton[@name="upgradeClose"]')
#     if elem.exists:
#         elem.click()
#         logger.info("关闭升级")