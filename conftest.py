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

import os,sys,subprocess,pytest,time,allure
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
            f2 = open(path.Cache_img_path2, 'rb').read()
            allure.attach(f2, '失败截图', allure.attachment_type.PNG)
            cb = open(path.log_path,'rb').read()
            c = cb.decode("utf-8","ignore")
            allure.attach(c, 'APPlog', allure.attachment_type.TEXT)
        except Exception as e:
            print(e,"截图或log抓取失败")




