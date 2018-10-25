# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_component import Component
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Common01(unittest.TestCase):
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
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model1()
        component.click_run()
        BasePage.warning_text(self)

    def test_common_1b1(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model4()
        component.click_run()
        BasePage.no_warning_text(self)
        component.click_close_result()

    def test_common_1b2(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model4()
        component.click_jishuanzujian5()
        component.click_peizhi5()
        time.sleep(1)
        component.click_peizhi5_1()
        component.click_peizhi5_12()
        component.click_jishuanzujian1()
        component.click_shuchu1()
        component.click_peizhi1()
        component.click_peizhi1_2()
        BasePage.get_windows_img(self)

    def test_common_2a(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model2()
        component.click_run()
        BasePage.no_warning_text(self)
        component.click_close_result()

    def test_common_2b(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model2()
        component.click_jishuanzujian1()
        component.click_preview1()
        component.click_preview1now()
        BasePage.no_warning_text(self)
        component.click_close_result()

    def test_common_2c(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model2()
        component.click_jishuanzujian1()
        component.click_delete1()
        BasePage.get_windows_img(self)

    def test_common_2d(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model2()
        component.click_jishuanzujian1()
        component.click_peizhi1()
        component.click_peizhi1_1()
        component.click_peizhi1_12()
        component.click_shuchu1()
        component.compair_ziduan('通关时间2')
        component.click_ziduan1()
        component.click_shuchu_1()
        component.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_common_2e(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model2()
        component.click_jishuanzujian1()
        component.click_shuchu1()
        component.click_ziduan_1()
        component.click_chehui_1()
        time.sleep(1)
        component.click_run()
        BasePage.warning_text(self)

    def test_common_2f(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model2()
        component.click_jishuanzujian1()
        component.click_shuchu1()
        component.click_big1()
        BasePage.get_windows_img(self)
        component.click_small1()


    def test_common_2g(self):
        #搜索
        pass

    def test_common_2h(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model1()
        component.click_shujuyuan2()
        component.click_shuchu2()
        component.click_choose_lla2()
        component.click_chehui_2()
        component.click_shujuyuan2()
        component.click_jishuanzujian1()
        component.click_shuchu1()
        component.click_peizhi1()
        BasePage.get_windows_img(self)
        component.click_run()
        BasePage.warning_text(self)

    def test_common_3a(self):
        component = Component(self.driver)
        component.click_model()
        component.click_public_model()
        component.double_model3()
        component.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

if __name__ == '__main__':
    unittest.main()