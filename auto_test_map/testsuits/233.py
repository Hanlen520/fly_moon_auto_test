import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from public.logger import Logger
# i = 1
for i in range(9,49):
    Logger().info('modle%d*******************************************' % i)
    chrome_driver_path = 'D:\\sss\\autoTestForMAP\\auto_test_map\\tools\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver_path)
    driver.maximize_window()
    driver.get('http://192.168.0.27:8080/#/login')
    time.sleep(1)
    username = 'modle2'
    password = '123456'
    driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/form/input[1]').send_keys(username)
    driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/form/input[2]').send_keys(password)
    driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[2]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="tab-model"]').click()
    time.sleep(1)
    d = driver.find_element_by_xpath('//*[@id="pane-model"]/div[2]/ul[1]/li[%d]/a' % i)
    ActionChains(driver).double_click(d).perform()
    driver.find_element_by_xpath('/html/body/div/div[2]/nav/ul/li[4]/a').click()
    time.sleep(2)
    i += 1
    wait = ui.WebDriverWait(driver, 120)
    wait.until(lambda dr: driver.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div').is_displayed())
    try:
        time.sleep(2)
        error_mes = driver.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/h2')
        Logger().info(error_mes.text)
        Logger().info('!!!!!!!!!!!!!!!!!!!!!test false!!!!!!!!!!!!!!!!!!!!!!.出现错误提示框')
    except Exception as e:
        driver.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[1]/span').is_displayed()  # 计算结果框:
        link = driver.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[1]/span')  # 关闭
        calculate_text = driver.find_element_by_xpath('//*[@id="#modals-container"]/div/div/div[2]/div/div[2]/table/thead/tr[1]/th')  # 计算时间
        result_text = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/p')  # 结果条数
        Logger().info('%s' % calculate_text.text)
        Logger().info('%s' % result_text.text)
        Logger().info('关闭计算结果')
        Logger().info("！！！！！！！！！！！Test pass.提示框未出现！！！！！！！！！！！！")
        pass
    Logger().info('*******************************************')
    driver.quit()
    continue


