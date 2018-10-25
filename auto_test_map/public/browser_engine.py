# coding=utf-8
import os.path
import time
import configparser
from selenium import webdriver
from public.logger import Logger
#logger = Logger(logger="browser_engine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    def __init__(self, driver):
        self.driver = driver
        # read the browser type from config.ini file, return the driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        Logger().info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        Logger().info("The test server url is: %s" % url)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            Logger().info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            Logger().info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            Logger().info("Starting IE browser.")
        driver.maximize_window()  # 窗口最大化
        Logger().info("Maximize the current window.")
        driver.get(url)
        Logger().info("Open url: %s" % url)
        driver.implicitly_wait(10)
        Logger().info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        Logger().info("Now, Close and quit the browser.")
        self.driver.quit()