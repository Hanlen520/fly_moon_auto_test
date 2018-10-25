# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 0016 9:17
# @Author  : 郝一阳
# @FileName: test_wifi.py
# @Software: PyCharm

# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_wifi import Wifi
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Wifi01(unittest.TestCase):
    #@classmethod
    def setUp(self):
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

    def test_wifi_1a(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model1()
        wifi.click_run()
        BasePage.warning_text(self)

    def test_wifi_2a(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_wifi_2b(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_jishuanzujian1()
        wifi.click_preview1()
        wifi.click_preview1now()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_wifi_2c(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_jishuanzujian1()
        wifi.click_delete1()
        BasePage.get_windows_img(self)

    def test_wifi_2d1(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_jishuanzujian1()
        wifi.click_peizhi1()
        wifi.click_peizhi1_1()
        wifi.click_peizhi1_81()
        BasePage.get_windows_img(self)
        wifi.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_wifi_2d2(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_jishuanzujian1()
        wifi.click_peizhi1()
        wifi.click_peizhi1_4()
        wifi.click_peizhi1_41()
        BasePage.get_windows_img(self)
        wifi.click_run()
        BasePage.no_warning_text(self)

    def test_wifi_2d3(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_jishuanzujian1()
        wifi.click_peizhi1()
        wifi.click_peizhi1_1()
        wifi.click_peizhi1_12()
        BasePage.get_windows_img(self)
        wifi.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_wifi_2e(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_jishuanzujian1()
        wifi.click_peizhi1()
        wifi.click_peizhi1_2()
        wifi.click_peizhi1_21()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_wifi_2f(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model2()
        wifi.click_shujuyuan2()
        wifi.click_shuchu2()
        wifi.click_choose_lla2()
        wifi.click_chehui_2()
        wifi.click_peizhi1()
        BasePage.get_windows_img(self)
        wifi.click_run()
        BasePage.warning_text(self)

    def test_wifi_2g1(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model3()
        wifi.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_wifi_2g2(self):
        wifi = Wifi(self.driver)
        wifi.click_model()
        wifi.click_public_model()
        wifi.double_model3()
        wifi.click_jishuanzujian1()
        wifi.click_peizhi1()
        wifi.click_peizhi1_2()
        wifi.click_peizhi1_21()
        wifi.click_jishuanzujian5()
        wifi.click_peizhi5()
        wifi.click_shuchu5()
        BasePage.get_windows_img(self)
        wifi.click_run()
        BasePage.warning_text(self)
        BasePage.click_close_result(self)



if __name__ == '__main__':
    unittest.main()