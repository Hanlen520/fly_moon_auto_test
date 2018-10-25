# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 0016 11:11
# @Author  : 郝一阳
# @FileName: test_car.py
# @Software: PyCharm

# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_car import Car
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Car01(unittest.TestCase):
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

    def test_car_1a(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model1()
        car.click_run()
        BasePage.warning_text(self)

    def test_car_2a(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_car_2b(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_jishuanzujian1()
        car.click_preview1()
        car.click_preview1now()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_car_2c(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_jishuanzujian1()
        car.click_delete1()
        BasePage.get_windows_img(self)

    def test_car_2d1(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_jishuanzujian1()
        car.click_peizhi1()
        car.click_peizhi1_1()
        car.click_peizhi1_11()
        BasePage.get_windows_img(self)
        car.click_run()
        BasePage.warning_text(self)

    # def test_car_2d2(self):
    #     car = Car(self.driver)
    #     car.click_model()
    #     car.click_public_model()
    #     car.double_model2()
    #     car.click_jishuanzujian1()
    #     car.click_peizhi1()
    #     car.click_ziduan_1()
    #     car.click_chehui_1()
    #     BasePage.get_windows_img(self)
    #     car.click_run()
    #     BasePage.warning_text(self)

    def test_car_2d3(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_jishuanzujian1()
        car.click_peizhi1()
        car.type_peizhi1_6('1')
        time.sleep(1)
        BasePage.get_windows_img(self)
        car.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_car_2e(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_jishuanzujian1()
        car.click_peizhi1()
        car.click_peizhi1_7()
        car.click_peizhi1_71()
        car.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_car_2f(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model2()
        car.click_shujuyuan2()
        car.click_shuchu2()
        car.click_choose_lla2()
        car.click_chehui_2()
        car.click_peizhi1()
        BasePage.get_windows_img(self)
        car.click_run()
        BasePage.get_warning_img(self)

    def test_car_2g1(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model3()
        car.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_car_2g2(self):
        car = Car(self.driver)
        car.click_model()
        car.click_public_model()
        car.double_model3()
        car.click_jishuanzujian1()
        car.click_peizhi1()
        car.click_peizhi1_7()
        car.click_peizhi1_71()
        car.click_jishuanzujian5()
        car.click_peizhi5()
        car.click_shuchu5()
        car.compair_ziduan4_1('旅客_姓名2_1')
        BasePage.get_windows_img(self)
        car.click_run()
        BasePage.zero_text(self)


if __name__ == '__main__':
    unittest.main()