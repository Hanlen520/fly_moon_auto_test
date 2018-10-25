# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 0005 11:11
# @Author  : 郝一阳
# @FileName: test_condition.py
# @Software: PyCharm
# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_condition import Condition
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Condition01(unittest.TestCase):
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

    def test_condition_1a(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model1()
        condition.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_condition_1b1(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model3()
        condition.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_condition_1b2(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model3()
        condition.click_jishuanzujian1()
        condition.click_peizhi1()
        condition.click_peizhi1_4()
        condition.click_peizhi1_42()
        condition.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)
        BasePage.get_windows_img(self)

    def test_condition_1b3(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model3()
        condition.click_jishuanzujian1()
        condition.click_shuchu1()
        condition.click_zhiduan1_1()
        condition.click_chehui_1()
        condition.click_run()
        BasePage.warning_text(self)

    def test_condition_2a(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model2()
        condition.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_condition_2b(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model2()
        condition.click_jishuanzujian1()
        condition.click_preview1()
        condition.click_preview1now()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_condition_2c(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model2()
        condition.click_jishuanzujian1()
        condition.click_delete1()
        BasePage.get_windows_img(self)

    # def test_condition_2d(self):
    #     condition = Condition(self.driver)
    #     condition.click_model()
    #     condition.click_public_model()
    #     condition.double_model2()
    #     condition.click_jishuanzujian1()
    #     condition.click_peizhi1()
    #     condition.click_ziduan1()
    #     condition.click_shuchu_1()
    #     BasePage.get_windows_img(self, '2d-')
    #     condition.click_run()
    #     BasePage.no_warning_text(self)
    #     BasePage.click_close_result(self)

    def test_condition_2e(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model2()
        condition.click_jishuanzujian1()
        condition.click_shuchu1()
        condition.click_choose_lla1()
        condition.click_chehui_1()
        time.sleep(1)
        condition.click_run()
        BasePage.warning_text(self)

    def test_condition_2f(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model2()
        condition.click_jishuanzujian1()
        condition.click_shuchu1()
        condition.type_search1('重')
        condition.compair_ziduan1('重点人_姓名3')

    def test_condition_2g(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model2()
        condition.click_jishuanzujian1()
        condition.click_shuchu1()
        condition.click_big1()
        BasePage.get_windows_img(self)
        condition.click_small1()

    def test_condition_2h(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model3()
        condition.click_shujuyuan2()
        condition.click_shuchu2()
        condition.click_zhiduan2_1()
        condition.click_chehui_2()
        condition.click_run()
        BasePage.warning_text(self)

    def test_condition_2i1(self):
        condition = Condition(self.driver)
        condition.click_model()
        condition.click_public_model()
        condition.double_model3()
        condition.click_jishuanzujian1()
        condition.click_peizhi1()
        condition.click_peizhi1_3()
        condition.click_peizhi1_35()
        time.sleep(1)
        condition.click_peizhi1_4()
        condition.click_peizhi1_41()
        time.sleep(1)
        condition.click_peizhi1_7()
        condition.click_peizhi1_71()
        BasePage.get_windows_img(self)
        condition.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)


if __name__ == '__main__':
    unittest.main()