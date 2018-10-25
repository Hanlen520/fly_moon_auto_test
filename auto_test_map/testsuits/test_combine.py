# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_combine import Combine
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Combine01(unittest.TestCase):
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

    def test_combine_1a(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model1()
        combine.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_combine_1b1(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model3()
        combine.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_combine_1b2(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model4()
        combine.click_jishuanzujian5()
        combine.click_peizhi5()
        combine.click_ziduan5_1()
        combine.click_chehui_5()
        combine.click_jishuanzujian1()
        combine.click_peizhi1()
        BasePage.get_windows_img(self)

    def test_combine_2a(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model2()
        combine.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_combine_2b(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model2()
        combine.click_jishuanzujian1()
        combine.click_preview1()
        combine.click_preview1now()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_combine_2c(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model2()
        combine.click_jishuanzujian1()
        combine.click_delete1()
        BasePage.get_windows_img(self)

    def test_combine_2d(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model2()
        combine.click_jishuanzujian1()
        combine.click_peizhi1()
        combine.click_ziduan1()
        combine.click_shuchu_1()
        BasePage.get_windows_img(self)
        combine.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

    def test_combine_2e(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model2()
        combine.click_jishuanzujian1()
        combine.click_peizhi1()
        combine.click_choose_lla1()
        combine.click_chehui_1()
        time.sleep(1)
        combine.click_run()
        BasePage.warning_text(self)

    def test_combine_2f(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model2()
        combine.click_jishuanzujian1()
        combine.click_peizhi1()
        combine.type_search1('卡口')
        combine.compair_ziduan1('卡口2')


    def test_combine_3a(self):
        combine = Combine(self.driver)
        combine.click_model()
        combine.click_public_model()
        combine.double_model3()
        combine.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

if __name__ == '__main__':
    unittest.main()