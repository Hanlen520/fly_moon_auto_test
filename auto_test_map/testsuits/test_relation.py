# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 0012 9:39
# @Author  : 郝一阳
# @FileName: test_relation.py
# @Software: PyCharm
# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_relation import Relation
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Relation01(unittest.TestCase):
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

    def test_common_1a(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model1()
        relation.click_run()
        BasePage.warning_text(self)

    def test_common_2a(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_run()
        BasePage.no_warning_text(self)
        relation.click_close_result()

    def test_common_2b(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_preview1()
        relation.click_preview1now()
        BasePage.no_warning_text(self)
        relation.click_close_result()

    def test_common_2c(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_delete1()
        BasePage.get_windows_img(self)

    def test_common_2d1(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_peizhi1()
        relation.click_peizhi1_2()
        relation.click_peizhi1_22()
        relation.click_shuchu1()
        relation.compair_ziduan1('旅客_姓名2')
        # relation.click_ziduan1()
        # relation.click_shuchu_1()
        BasePage.get_windows_img(self)
        time.sleep(1)
        relation.click_run()
        BasePage.no_warning_text(self)
        relation.click_close_result()

    def test_common_2d2(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_peizhi1()
        relation.click_peizhi1_1()
        relation.click_peizhi1_12()
        relation.click_shuchu1()
        relation.compair_ziduan1('旅客_姓名2')
        BasePage.get_windows_img(self)
        time.sleep(1)
        relation.click_run()
        BasePage.warning_text(self)



    def test_common_2e(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_shuchu1()
        relation.click_choose_lla1()
        relation.click_chehui_1()
        time.sleep(1)
        relation.click_run()
        BasePage.warning_text(self)

    def test_common_2f(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_shuchu1()
        relation.click_big1()
        BasePage.get_windows_img(self)
        relation.click_small1()


    def test_common_2g(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_jishuanzujian1()
        relation.click_shuchu1()
        relation.type_search1('房间')
        relation.compair_ziduan1('房间_编号2')



    def test_common_2h(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model2()
        relation.click_shujuyuan2()
        relation.click_shuchu2()
        relation.click_choose_lla2()
        time.sleep(1)
        relation.click_chehui_2()
        time.sleep(1)
        relation.click_shujuyuan2()
        relation.click_jishuanzujian1()
        relation.click_shuchu1()
        relation.click_peizhi1()
        BasePage.get_windows_img(self)
        relation.click_run()
        BasePage.warning_text(self)

    def test_common_3a1(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model3()
        relation.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_common_3a2(self):
        relation = Relation(self.driver)
        relation.click_model()
        relation.click_public_model()
        relation.double_model3()
        relation.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

if __name__ == '__main__':
    unittest.main()