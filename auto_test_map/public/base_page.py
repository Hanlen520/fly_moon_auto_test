# coding=utf-8
# @Author  : 郝一阳

import time

from selenium.webdriver.support.select import Select
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from public.browser_engine import BrowserEngine
import os.path
from public.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import configparser


#定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

#退出浏览器
    def quit_browser(self):
        self.driver.quit()

# 浏览器前进操作
    def forward(self):
        self.driver.forward()
        Logger().info("Click forward on current page.")

# 浏览器后退操作
    def back(self):
        self.driver.back()
        Logger().info("Click back on current page.")

# 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        Logger().info("wait for %d seconds." % seconds)

# 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            Logger().info("Closing and quit the browser.")
        except NameError as e:
            Logger().error("Failed to quit the browser with %s" % e)


# 部分错误图片保存
    def get_warning_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenpicture/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            Logger().info("Had take screenshot and save to folder : /screenpicture")
            print(screen_name)
        except NameError as e:
            Logger().error("Failed to take screenpicture! {}".format(e))
            self.get_windows_img()

# 截图保存1
#     def get_windows_img(self, text):
#         time.sleep(1)
#         file_path = os.path.dirname(os.path.abspath('.')) + '/screenpicture/'
#         rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#         screen_name = file_path + text + rq + '.png'
#         try:
#             self.driver.get_screenshot_as_file(screen_name)
#             Logger().info("Had take screenshot and save to folder : /screenpicture")
#         except NameError as e:
#             Logger().error("Failed to take screenshot! %s" % e)
#             self.get_warning_img()

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenpicture/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            Logger().info("Had take screenshot and save to folder : /screenpicture")
            print(screen_name)
        except NameError as e:
            Logger().error("Failed to take screenpicture! {}".format(e))
            self.get_windows_img()

#截图保存2
    def get_windows_img2(self):
        time.sleep(1)
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshort2/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            Logger().info("Had take screenshot and save to folder : /screenshort2")
        except NameError as e:
            Logger().error("Failed to take screenshot! %s" % e)
            self.get_windows_img2()

#截图保存3
    def get_windows_img3(self):
        time.sleep(1)
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshort3/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            Logger().info("Had take screenshot and save to folder : /screenshort3")
        except NameError as e:
            Logger().error("Failed to take screenshot! %s" % e)
            self.get_windows_img3()

# 定位元素方法
    def find_element(self, selector):
        element = ''

        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                Logger().info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                Logger().error("NoSuchElementException: %s" % e)
                self.get_warning_img()

        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "cl" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "c" or selector_by == "css_selector":
            element = self.driver.find_element_by_css_selector(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                Logger().info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                Logger().error("NoSuchElementException: %s" % e)
                self.get_warning_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

#定位元素隐性等待时间
    def element_wait(self, selector, secs=1):
        """
        Waiting for an element to display.
        Usage:
        driver.element_wait("id->kw",10)
        """
        if "=>" not in selector:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = selector.split("=>")[0].strip()
        value = selector.split("=>")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(selector, secs)

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)),messages)
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)),messages)
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),messages)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")


    # 文本输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            Logger().info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            Logger().error("Failed to type in input box with %s" % e)
            self.get_warning_img()

# 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            Logger().info("Clear text in input box before typing.")
        except NameError as e:
            Logger().error("Failed to clear in input box with %s" % e)
            self.get_warning_img()

# 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            #Logger().info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            Logger().error("Failed to enter the element with %s" % e)

# 点击元素js方法1
    def jsclick(self, selector):
        el = self.find_element(selector)
        dr = BrowserEngine(self.driver).driver
        dr.execute_script('$(arguments[0]).click()', el)
        Logger().info('js点击方法2')

# 字段核对，后期优化
    def findtext(self,selector ,name):
        try:
            el = self.find_element(selector)
            dr = BrowserEngine(self.driver).driver
            # wait = ui.WebDriverWait(dr, 3)  #等待搜索结果显示3秒
            # wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="ioper_03_1_b"]/div/div[1]/div[2]/label[1]/span[2]').is_displayed())
            text = el.text
            if text == name:
                Logger().info('搜索字段为' + text)
            else:
                raise ValueError('搜索字段不匹配!!!!!!!!!!!!!!!!!!')
        except Exception:
            raise ValueError('无搜索结果')

# #组件1输出框搜索核对搜索结果
#     def findtext_shuchu(self ,name):
#         try:
#             dr = BrowserEngine(self.driver).driver
#             time.sleep(1)
#             #wait = ui.WebDriverWait(dr, 3)
#             #wait.until(lambda dr: dr.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/ul/li[1]/span').is_displayed())
#             #el = self.element_wait(selector)
#             text = dr.find_element_by_xpath('//*[@id="ioper_03_1_b"]/div/div[1]/div[2]/label[1]/span[2]').text
#             print(text)
#             if text == name:
#                 Logger().info('搜索字段为' + text)
#             else:
#                 raise ValueError('搜索字段不匹配!!!!!!!!!!!!!!!!!!')
#         except Exception:
#             raise ValueError('无搜索结果')
#
# #组件1配置框搜索核对搜索结果
#     def findtext_peizhi(self ,name):
#         try:
#             dr = BrowserEngine(self.driver).driver
#             wait = ui.WebDriverWait(dr, 3)
#             wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="ioper_04_1_a"]/div/div[1]/div[3]/label[1]/span[2]').is_displayed())
#             text = dr.find_element_by_xpath('//*[@id="ioper_04_1_a"]/div/div[1]/div[3]/label[1]/span[2]').text
#             if text == name:
#                 Logger().info('搜索字段为' + text)
#             else:
#                 raise ValueError('搜索字段不匹配!!!!!!!!!!!!!!!!!!')
#         except Exception:
#             raise ValueError('无搜索结果')

#获取文本
    def get_text(self, selector):
        el = self.find_element(selector)
        try:
            Logger().info('%s' % el.text)
        except NameError as e:
            Logger().error("Failed to enter the element with %s" % e)

#enter
    def enter(self, selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.ENTER)
        except NameError as e:
            Logger().error("Failed to click the element with %s" % e)

#右击
    def right_click(self, selector):

        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).context_click(el).perform()
            Logger().info("The element \' %s \' was right_clicked." % el.text)
        except NameError as e:
            Logger().error("Failed to click the element with %s" % e)

#双击
    def click_twice(self, selector):

        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).double_click(el).perform()
            Logger().info("The element \' %s \' was double_clicked." % el.text)
        except NameError as e:
            Logger().error("Failed to click the element with %s" % e)

#鼠标移动
    def move_click(self,selector,x,y):

        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,x,y).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def test_click(self,selector,x,y):

        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,x,y).context_click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

#鼠标点击
    def acclick(self,selector):

        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).click(el).perform()
            Logger().info("The element was acclick." )
        except NameError as e:
            Logger().error("Failed to acclick the element with %s" % e)


# 获取网页标题
    def get_page_title(self):
        Logger().info("Current page title is %s" % self.driver.title)
        return self.driver.title

# 等待时间
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        Logger().info("Sleep for %d seconds" % seconds)

#登录操作单独放在基类，考虑加入进入公有模型操作
    def login(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        username = config.get("userInfo", "username")
        Logger().info("username is %s." % username)
        password = config.get("userInfo", "password")
        Logger().info("The password is: %s" % password)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/form/input[1]').send_keys(
            username)
        Logger().info('输入账户AlphaGo')
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/form/input[2]').send_keys(
            password)
        Logger().info('输入密码123456')
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/button').click()
        Logger().info("点击登录")
        time.sleep(1)


    '''*******
    断言用提示框
    *******'''
    warning_word = '/html/body/div[19]/div/h2'

    #应当有提示框时
    def warning_text(self):
        from selenium.common.exceptions import NoSuchElementException
        dr = BrowserEngine(self.driver).driver
        wait = ui.WebDriverWait(dr, 30)
        wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/h2').is_displayed())
        #error_mes = dr.find_element_by_xpath('/html/body/div[19]/div/h2')
        try:
            error_mes = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/h2')
            Logger().info('！！！！！！！！！Test pass.提示框出现！！！！！！！！！')
        except Exception as e:
            BasePage.get_warning_img(self)
            raise ValueError("!!!!!!!!!!!!!!!!!!!!!!Test fail!!!!!!!!!!!!!!!!!!!!!!!!!!!.提示框未出现", format(e))
        else:
            Logger().info(error_mes.text)
            print('test pass')
            return True

    def zero_text(self):
        from selenium.common.exceptions import NoSuchElementException
        dr = BrowserEngine(self.driver).driver
        wait = ui.WebDriverWait(dr, 120)
        wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/span').is_displayed())
        #error_mes = dr.find_element_by_xpath('/html/body/div[19]/div/h2')
        try:
            error_mes = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/p')
            Logger().info('！！！！！！！！！Test pass.计算结果为0！！！！！！！！！')
            link = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/span')  #关闭
            link.click()
        except Exception as e:
            BasePage.get_warning_img(self)
            raise ValueError("!!!!!!!!!!!!!!!!!!!!!!Test fail!!!!!!!!!!!!!!!!!!!!!!!!!!!", format(e))
        # else:
        #     Logger().info(error_mes.text)
        #     print('test pass')
        #     return True

    #应当无提示框时
    '''raise注释掉了是什么鬼'''
    def no_warning_text(self):
        from selenium.common.exceptions import NoSuchElementException
        dr = BrowserEngine(self.driver).driver
        #wait = ui.WebDriverWait(dr, 120)
        #wait.until(lambda dr: dr.find_element_by_xpath('/html/body/div[19]/div/h2').is_displayed())
        time.sleep(2)
        try:
            error_mes = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/h2')
        except Exception as e:
            Logger().info("！！！！！！！！！！！Test pass.提示框未出现！！！！！！！！！！！！")

        else:
            BasePage.get_warning_img(self)
            Logger().info(error_mes.text)
            raise ValueError('!!!!!!!!!!!!!!!!!!!!!test false!!!!!!!!!!!!!!!!!!!!!!.出现错误提示框')
            #print('!!!!!!!!!!!!!!!!!!!!!test false!!!!!!!!!!!!!!!!!!!!!!.出现错误提示框')
            #return False

    #关闭计算结果
    # def click_close_result(self):
    #     #calculate_text = 'x=>/html/body/div[3]/p[1]'
    #     #result_text = 'x=>/html/body/div[12]/div[2]/div/div[1]/p/span'
    #     dr = BrowserEngine(self.driver).driver
    #     wait = ui.WebDriverWait(dr, 120)
    #     wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div').is_displayed())
    #     try:
    #         dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[1]/span').is_displayed()   #计算结果框:
    #         link = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[1]/span')  #关闭
    #         BasePage.get_windows_img(self)
    #         calculate_text = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[2]/table/thead/tr[1]/th')     #计算时间
    #         result_text = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/p')   #结果条数
    #         link.click()
    #         #dr.execute_script('$(arguments[0]).click()', link)
    #         Logger().info('%s' % calculate_text.text)
    #         Logger().info('%s' % result_text.text)
    #         Logger().info('关闭计算结果')
    #     except Exception as e:
    #         try:
    #             dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/span').is_displayed()
    #             reason_text = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/p')
    #             Logger().info('%s' % reason_text.text)
    #             dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/span').click()
    #         except Exception as e:
    #             raise ValueError('time out!!!!!!!!!!!!!!!!!!')

    def click_close_result(self):
        #calculate_text = 'x=>/html/body/div[3]/p[1]'
        #result_text = 'x=>/html/body/div[12]/div[2]/div/div[1]/p/span'
        dr = BrowserEngine(self.driver).driver
        wait = ui.WebDriverWait(dr, 120)
        wait.until(lambda dr: dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div').is_displayed())
        try:
            dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[1]/span').is_displayed()   #计算结果框:
            link = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[1]/span')  #关闭
            BasePage.get_windows_img(self)
            calculate_text = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[2]/table/thead/tr[1]/th')     #计算时间
            result_text = dr.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/p')   #结果条数
            link.click()
            #dr.execute_script('$(arguments[0]).click()', link)
            Logger().info('%s' % calculate_text.text)
            Logger().info('%s' % result_text.text)
            Logger().info('关闭计算结果')
        except Exception as e:
            if  dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/span').is_displayed():
                reason_text = dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/p')
                Logger().info('%s' % reason_text.text)
                dr.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div/span').click()
                raise ValueError('计算结果为0!!!!!!!!!!!!!!!!!!')
            else:
                raise ValueError('time out!!!!!!!!!!!!!!!!!!')

    #下拉框
    def choose_selector(self,selector ,text):
        el = self.find_element(selector)
        #s = driver.find_element_by_id("nr")
        Select(el).select_by_index(text)

    #日期栏核查，或许暂时还用不了吧
    # def warning_date(self, selector):
    #     dr = BrowserEngine(self.driver).driver
    #     wait = ui.WebDriverWait(dr, 15)
    #     wait.until(lambda dr: selector.is_displayed())
    #     try:
    #         error_mes = selector
    #     except Exception as e:
    #         BasePage.get_warning_img(self)
    #         print("!!!!!!!!!!!!!!!!!!!!!!Test fail!!!!!!!!!!!!!!!!!!!!!!!!!!!.日期框未出现", format(e))
    #         return False

    '''
    计算组件与数据源专用
    '''

    def ji_peizhi(self, selector):

        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,34,-20).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def ji_shuchu(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,68,17).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def ji_delete(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,-34,0).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def ji_preview(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,0,68).click().perform()
            time.sleep(1)
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,-90,164).context_click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def shu_shuchu(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,45,20).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def shu_peizhi(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,45,-5).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def shu_delete(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,-25,-5).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def select1(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,50,36).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def select2(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,50,70).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def select3(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,50,104).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def select4(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,50,138).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def select5(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,50,172).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def shuchu(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,242,42).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)

    def chehui(self, selector):
        el = self.find_element(selector)
        try:
            ActionChains(BrowserEngine(self.driver).driver).move_to_element_with_offset(el,242,83).click().perform()
            Logger().info("The element \' %s \' was moved." % el.text)
        except NameError as e:
            Logger().error("Failed to move to the element with %s" % e)



'''
修改元素属性、获取属性信息
'''
# driver.execute_script("arguments[0].style=arguments[1]",t1,"draggable: true;")
# ll2 = t0.get_attribute("draggable")