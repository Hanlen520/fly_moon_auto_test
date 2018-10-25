# coding=utf-8
import time
import unittest
from public.browser_engine import BrowserEngine
from pageobjects.page_filter import Filter
from public.base_page import BasePage
from public.logger import Logger
from selenium import webdriver
#import HTMLTestRunner

class Fillter01(unittest.TestCase):
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
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_run()
        BasePage.no_warning_text(self)
        filter.click_close_result()

    def test_common_1b(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_jishuanzujian1()
        filter.click_preview1()
        filter.click_preview1now()
        BasePage.no_warning_text(self)
        filter.click_close_result()

    def test_common_1c(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_jishuanzujian1()
        filter.click_delete1()
        BasePage.get_windows_img(self)

    def test_common_1d(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_jishuanzujian1()
        filter.click_peizhi1()
        filter.click_peizhi1_1()
        filter.click_peizhi1_13()
        filter.click_peizhi1_2()
        filter.click_peizhi1_21()
        filter.type_peizhi1_3('a')
        filter.click_shuchu1()
        filter.compair_ziduan1('车辆_车牌号码2')
        time.sleep(1)
        filter.click_ziduan1()
        filter.click_shuchu_1()
        filter.click_run()
        BasePage.no_warning_text(self)
        BasePage.zero_text(self)

    def test_common_1e(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_jishuanzujian1()
        filter.click_shuchu1()
        filter.click_choose_lla1()
        filter.click_chehui_1()
        time.sleep(1)
        filter.click_run()
        BasePage.warning_text(self)

    def test_common_1f(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_jishuanzujian1()
        filter.click_shuchu1()
        filter.click_big1()
        BasePage.get_windows_img(self)
        filter.click_small1()


    def test_common_1g(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_jishuanzujian1()
        filter.click_shuchu1()
        filter.type_search1('卡口')
        filter.compair_ziduan1('卡口2')


    def test_common_1i(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model1()
        filter.click_shujuyuan2()
        filter.click_shuchu2()
        filter.click_choose_lla2()
        filter.click_chehui_2()
        time.sleep(1)
        filter.click_jishuanzujian1()
        filter.click_shuchu1()
        filter.click_peizhi1()
        BasePage.get_windows_img(self)
        filter.click_run()
        BasePage.warning_text(self)

    def test_common_1h1(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model2()
        filter.click_run()
        BasePage.no_warning_text(self)
        filter.click_close_result()

    def test_common_1h2(self):
        filter = Filter(self.driver)
        filter.click_model()
        filter.click_public_model()
        filter.double_model2()
        filter.click_jishuanzujian1()
        filter.click_shuchu1()
        filter.click_shuchu_1()
        filter.click_ziduan_1()
        filter.click_chehui_1()
        filter.click_jishuanzhujian3()
        filter.click_shuchu3()
        filter.click_peizhi3()
        BasePage.get_windows_img(self)
        filter.click_run()
        BasePage.no_warning_text(self)
        BasePage.click_close_result(self)

if __name__ == '__main__':
    unittest.main()