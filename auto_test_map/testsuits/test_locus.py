# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 0012 14:21
# @Author  : 郝一阳
# @FileName: test_locus.py
# @Software: PyCharm
# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_locus import Locus
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Locus01(unittest.TestCase):
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

    def test_locus_1a(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model1()
        locus.click_run()
        BasePage.warning_text(self)

    def test_locus_2a(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_locus_2b(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_preview1()
        locus.click_preview1now()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_locus_2c(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_delete1()
        BasePage.get_windows_img(self)

    def test_locus_2d1(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_peizhi1()
        locus.click_peizhi1_1()
        locus.click_peizhi1_11()
        BasePage.get_windows_img(self)
        locus.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_locus_2d2(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_peizhi1()
        locus.click_ziduan_1()
        time.sleep(1)
        locus.click_chehui_1()
        BasePage.get_windows_img(self)
        locus.click_run()
        BasePage.warning_text(self)

    def test_locus_2d3(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_peizhi1()
        locus.type_search1('房')
        time.sleep(2)
        locus.compair_ziduan1('房间_编号2')
        BasePage.get_windows_img(self)
        locus.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_locus_2d4(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_peizhi1()
        locus.type_peizhi1_6('1')
        BasePage.get_windows_img(self)
        locus.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_locus_2e(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_jishuanzujian1()
        locus.click_peizhi1()
        locus.click_peizhi1_7()
        locus.click_peizhi1_71()
        time.sleep(1)
        locus.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_locus_2f(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model2()
        locus.click_shujuyuan2()
        locus.click_shuchu2()
        locus.click_choose_lla2()
        locus.click_chehui_2()
        locus.click_peizhi1()
        BasePage.get_windows_img(self)
        locus.click_run()
        BasePage.get_warning_img(self)

    def test_locus_2g1(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model3()
        locus.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_locus_2g2(self):
        locus = Locus(self.driver)
        locus.click_model()
        locus.click_public_model()
        locus.double_model3()
        locus.click_jishuanzujian1()
        locus.click_peizhi1()
        locus.click_peizhi1_7()
        time.sleep(5)
        locus.click_peizhi1_71()
        locus.click_jishuanzujian5()
        locus.click_peizhi5()
        locus.click_shuchu5()
        BasePage.get_windows_img(self)
        locus.click_run()
        BasePage.warning_text(self)
        BasePage.click_close_result(self)



if __name__ == '__main__':
    unittest.main()