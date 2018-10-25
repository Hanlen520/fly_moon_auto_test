# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 0009 17:54
# @Author  : 郝一阳
# @FileName: test_group.py
# @Software: PyCharm
# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_group import Group
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Group01(unittest.TestCase):
    #@classmethod
    def setUp(self):
        #time.sleep(1)
        #time.sleep(20)
        self.logger = Logger()
        self.logger.info('######### 发起进攻(　 ´-ω ･)▄︻┻┳══━一 ###############################')
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)
        BasePage.login(self)

    #@classmethod
    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        self.logger.info('######### 战斗结束o(▼皿▼メ;)o ###############################')



    def test_group_1a(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_run()
        BasePage.no_warning_text(self)
        group.click_close_result()

    def test_group_1b(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_jishuanzujian1()
        group.click_preview1()
        group.click_preview1now()
        BasePage.no_warning_text(self)
        group.click_close_result()

    def test_group_1c(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_jishuanzujian1()
        group.click_delete1()
        BasePage.get_windows_img(self)

    def test_group_1d(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_jishuanzujian1()
        group.click_peizhi1()
        group.click_peizhi1_1()
        group.click_peizhi1_12()
        group.click_shuchu1()
        group.compair_ziduan1('通关时间2')
        time.sleep(1)
        group.click_ziduan1()
        time.sleep(1)
        group.click_shuchu_1()
        group.click_run()
        BasePage.no_warning_text(self)
        group.click_close_result()

    def test_group_1e(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_jishuanzujian1()
        group.click_shuchu1()
        group.click_choose_lla1()
        group.click_chehui_1()
        time.sleep(1)
        group.click_run()
        BasePage.warning_text(self)

    def test_group_1f(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_jishuanzujian1()
        group.click_shuchu1()
        group.click_big1()
        BasePage.get_windows_img(self)
        group.click_small1()


    def test_group_1g(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_jishuanzujian1()
        group.click_shuchu1()
        group.type_search1('车辆')
        group.compair_ziduan1('车辆_车牌号码2')


    def test_group_1i(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model1()
        group.click_shujuyuan2()
        group.click_shuchu2()
        group.click_choose_lla2()
        group.click_chehui_2()
        time.sleep(1)
        group.click_jishuanzujian1()
        group.click_shuchu1()
        group.click_peizhi1()
        BasePage.get_windows_img(self)
        group.click_run()
        BasePage.warning_text(self)

    def test_group_1h1(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model2()
        group.click_run()
        BasePage.no_warning_text(self)
        group.click_close_result()

    def test_group_1h2(self):
        group = Group(self.driver)
        group.click_model()
        group.click_public_model()
        group.double_model2()
        group.click_jishuanzujian1()
        group.click_shuchu1()
        group.click_shuchu_1()
        group.click_ziduan_1()
        group.click_chehui_1()
        group.click_jishuanzhujian3()
        group.click_shuchu3()
        group.click_peizhi3()
        BasePage.get_windows_img(self)
        group.click_run()
        BasePage.warning_text(self)

if __name__ == '__main__':
    unittest.main()