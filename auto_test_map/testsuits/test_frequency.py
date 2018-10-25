# -*- coding: utf-8 -*-
# @Time    : 2018/7/6 0006 9:16
# @Author  : 郝一阳
# @FileName: test_frequency.py
# @Software: PyCharm
# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_frequency import Frenquency
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Frenquency01(unittest.TestCase):
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



    def test_frenquency_1a(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_run()
        BasePage.no_warning_text(self)
        frenquency.click_close_result()

    def test_frenquency_1b(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_jishuanzujian1()
        frenquency.click_preview1()
        frenquency.click_preview1now()
        BasePage.no_warning_text(self)
        frenquency.click_close_result()

    def test_frenquency_1c(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_jishuanzujian1()
        frenquency.click_delete1()
        BasePage.get_windows_img(self)

    def test_frenquency_1d(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_jishuanzujian1()
        frenquency.click_peizhi1()
        frenquency.click_peizhi1_1()
        time.sleep(1)
        frenquency.click_peizhi1_13()
        frenquency.click_peizhi1_2()
        time.sleep(1)
        frenquency.click_peizhi1_23()
        frenquency.type_peizhi1_3('1')
        time.sleep(1)
        frenquency.click_shuchu1()
        frenquency.compair_ziduan1('卡口2')
        time.sleep(1)
        frenquency.click_ziduan1()
        frenquency.click_shuchu_1()
        frenquency.click_run()
        BasePage.no_warning_text(self)
        frenquency.click_close_result()

    def test_frenquency_1e(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_jishuanzujian1()
        frenquency.click_shuchu1()
        frenquency.click_choose_lla1()
        frenquency.click_chehui_1()
        time.sleep(1)
        frenquency.click_run()
        BasePage.warning_text(self)

    def test_frenquency_1f(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_jishuanzujian1()
        frenquency.click_shuchu1()
        frenquency.click_big1()
        BasePage.get_windows_img(self)
        frenquency.click_small1()


    def test_frenquency_1g(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_jishuanzujian1()
        frenquency.click_peizhi1()
        frenquency.click_peizhi1_1()
        frenquency.click_peizhi1_13()
        frenquency.click_shuchu1()
        frenquency.type_search1('卡口')
        frenquency.compair_ziduan1('卡口2')


    def test_frenquency_1i(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model1()
        frenquency.click_shujuyuan2()
        frenquency.click_shuchu2()
        frenquency.click_choose_lla2()
        frenquency.click_chehui_2()
        time.sleep(1)
        frenquency.click_jishuanzujian1()
        frenquency.click_shuchu1()
        frenquency.click_peizhi1()
        BasePage.get_windows_img(self)
        frenquency.click_run()
        BasePage.warning_text(self)

    def test_frenquency_1h1(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model2()
        frenquency.click_run()
        BasePage.no_warning_text(self)
        frenquency.click_close_result()

    def test_frenquency_1h2(self):
        frenquency = Frenquency(self.driver)
        frenquency.click_model()
        frenquency.click_public_model()
        frenquency.double_model2()
        frenquency.click_jishuanzujian1()
        frenquency.click_shuchu1()
        time.sleep(1)
        frenquency.click_shuchu_1()
        frenquency.click_ziduan_1()
        frenquency.click_chehui_1()
        frenquency.click_jishuanzhujian3()
        frenquency.click_shuchu3()
        frenquency.click_peizhi3()
        BasePage.get_windows_img(self)
        frenquency.click_run()
        BasePage.warning_text(self)

if __name__ == '__main__':
    unittest.main()