# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_different import Different
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Different01(unittest.TestCase):
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
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model1()
        different.click_run()
        BasePage.warning_text(self)

    def test_common_1b1(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model3()
        different.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_common_1b2(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model3()
        time.sleep(1)
        different.click_jishuanzujian5()
        different.click_peizhi5()
        different.click_peizhi5_1()
        different.click_peizhi5_12()
        different.click_jishuanzujian1()
        different.click_shuchu1()
        different.click_peizhi1()
        different.click_peizhi1_2()
        BasePage.get_windows_img(self)

    def test_common_2a(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model2()
        different.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_common_2b(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model2()
        different.click_jishuanzujian1()
        different.click_preview1()
        different.click_preview1now()
        BasePage.no_warning_text(self)
        different.click_close_result()

    def test_common_2c(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model2()
        different.click_jishuanzujian1()
        different.click_delete1()
        BasePage.get_windows_img(self)

    def test_common_2d(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model2()
        different.click_jishuanzujian1()
        different.click_peizhi1()
        different.click_peizhi1_2()
        different.click_peizhi1_22()
        different.click_shuchu1()
        different.compair_ziduan1('通关时间2')
        different.click_ziduan1()
        different.click_shuchu_1()
        time.sleep(1)
        different.click_run()
        BasePage.no_warning_text(self)
        different.click_close_result()

    def test_common_2e(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model2()
        different.click_jishuanzujian1()
        different.click_shuchu1()
        different.click_ziduan_1()
        different.click_chehui_1()
        time.sleep(1)
        different.click_run()
        BasePage.warning_text(self)

    def test_common_2f(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model2()
        different.click_jishuanzujian1()
        different.click_shuchu1()
        different.click_big1()
        BasePage.get_windows_img(self)
        different.click_small1()


    def test_common_2g(self):
        #搜索
        pass

    def test_common_2h(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model1()
        different.click_shujuyuan2()
        different.click_shuchu2()
        different.click_choose_lla2()
        time.sleep(1)
        different.click_chehui_2()
        time.sleep(1)
        different.click_shujuyuan2()
        different.click_jishuanzujian1()
        different.click_shuchu1()
        different.click_peizhi1()
        BasePage.get_windows_img(self)
        different.click_run()
        BasePage.warning_text(self)

    def test_common_3a(self):
        different = Different(self.driver)
        different.click_model()
        different.click_public_model()
        different.double_model4()
        different.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

if __name__ == '__main__':
    unittest.main()