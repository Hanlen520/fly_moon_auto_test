# coding=utf-8
from public.base_page import BasePage
from public.logger import Logger
import time
import selenium.webdriver.support.ui as ui
from public.browser_engine import BrowserEngine
from public.logger import Logger
import os,sys,time
from selenium.webdriver.support import expected_conditions as EC

#碰撞求同
class Component(BasePage):
    '''***
    公有部分
    ***'''
    model = 'xpath=>//*[@id="tab-model"]'
    run = 'xpath=>/html/body/div/div[2]/nav/ul/li[4]/a'
    #close_result = 'css_selector=>div.modal-move:nth-child(2) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)'
    #calculate_text = 'x=>/html/body/div[3]/p[1]'
    #result_text = 'x=>/html/body/div[12]/div[2]/div/div[1]/p/span'
    public_model = 'x=>//*[@id="pane-model"]/ul/li[1]/span'
    #close_warning = 'x=>/html/body/div[19]/div/button[1]'


    def click_model(self):
        self.click(self.model)
        Logger().info('点击模型栏')

    def click_public_model(self):
        time.sleep(1)
        self.click(self.public_model)
        Logger().info('查看公有模型')

    def click_run(self):
        self.click(self.run)
        Logger().info('点击运行')

    def click_close_warning(self):
        self.click(self.close_warning)
        time.sleep(1)
        Logger().info('关闭提示框')


    '''*******
    碰撞求同模型
    *******'''
    common_model1 = 'xpath=>/html/body/div/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul[1]/li[36]'
    common_model2 = 'x=>/html/body/div/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul[1]/li[35]'
    common_model3 = 'x=>/html/body/div/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul[1]/li[34]'
    common_model4 = 'x=>/html/body/div/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul[1]/li[33]'
    common_model5 = 'x=>/html/body/div/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/ul[1]/li[32]'

    def double_model1(self):
        time.sleep(1)
        self.click_twice(self.common_model1)
        Logger().info('进入碰撞求同模型1(单数据源)')

    def double_model2(self):
        time.sleep(1)
        self.click_twice(self.common_model2)
        Logger().info('进入碰撞求同模型2（双数据源）')

    def double_model3(self):
        time.sleep(1)
        self.click_twice(self.common_model3)
        Logger().info('进入碰撞求同模型3（多数据源）')

    def double_model4(self):
        time.sleep(1)
        self.click_twice(self.common_model4)
        Logger().info('进入碰撞求同模型4（连接碰撞求同组件）')

    def double_model5(self):
        time.sleep(1)
        self.click_twice(self.common_model5)
        Logger().info('进入碰撞求同模型5（连接其它组件）')

    """*********
    连接两个数据源
    *********"""
    jishuanzujuan1 = 'x=>//*[@id="ioper_02_1"]'
    preview1 = 'x=>//*[@id="menu3_1"]'  #预览
    preview1now = 'x=>//*[@id="ioper_13_1_c"]/button'    #当前结果
    delete1 = 'x=>//*[@id="menu3_undefined"]'
    peizhi1 = 'x=>//*[@id="menu0_undefined"]'
    peizhi1_1 = 'x=>//*[@id="ioper_02_1_a"]/div/div[1]/div/div/input'
    peizhi1_2 = 'x=>//*[@id="ioper_02_1_a"]/div/div[2]/div/div/input'
    shuchu1 = 'x=>//*[@id="menu1_undefined"]'
    big1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[1]/div[3]/button'
    small1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[1]/div[3]/button'
    ziduan1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[1]/div[2]/label[1]/span[2]'
    ziduan_1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[3]/div/label/span[2]'
    shuchu_1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[2]/button[1]/i'
    chehui_1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[2]/button[2]/i'
    search1 = 'x=>//*[@id="ioper_02_1_b"]/div/div[1]/div[1]/input'

    shujuyuan2 = 'x=>//*[@id="cnode_1028_2"]'
    delete2 = 'x=>//*[@id="menu6_undefined"]'
    shuchu2 = 'x=>//*[@id="menu2_undefined"]'
    ziduan2 = 'x=>//*[@id="cnode_1028_2_b"]/div/div[1]/div[3]/label[1]/span[2]'
    ziduan_2 = 'x=>//*[@id="cnode_1028_2_b"]/div/div[3]/div[2]/label[1]/span[2]'
    choose_all2 = 'x=>//*[@id="cnode_1028_2_b"]/div/div[1]/label/span[1]/span'
    choose_lla2 = 'x=>//*[@id="cnode_1028_2_b"]/div/div[2]/button[2]/i'
    shuchu_2 = 'x=>//*[@id="cnode_1028_2_b"]/div/div[2]/button[1]/i'
    chehui_2 = 'x=>//*[@id="cnode_1028_2_b"]/div/div[2]/button[2]/i'

    shujuyuan3 = 'x=>//*[@id="cnode_1028_3"]'
    delete3 = 'x=>//*[@id="menu5_3"]'



    '''
    碰撞求同1
    '''
    def click_jishuanzujian1(self):
        self.click(self.jishuanzujuan1)
        Logger().info('打开碰撞求同组件的环形菜单')

    def click_preview1(self):
        self.move_click(self.jishuanzujuan1,0,68)
        Logger().info('点击预览')

    def click_preview1now(self):
        self.click(self.preview1now)
        Logger().info('预览计算')

    def click_delete1(self):
        self.move_click(self.jishuanzujuan1, -34,0)
        Logger().info('点击删除')


    def click_peizhi1(self):
        self.move_click(self.jishuanzujuan1,34,-20)
        Logger().info('查看碰撞求同配置框')


    def click_peizhi1_1(self):
        self.click(self.peizhi1_1)
        Logger().info('查看配置下拉框1')

    def compair_ziduan(self, name):
        self.findtext(self.ziduan1 ,name)
        #assert mes == u'%s' % txt
        Logger().info('对比搜索字段')

    def click_peizhi1_2(self):
        self.click(self.peizhi1_2)
        time.sleep(1)
        Logger().info('查看配置下拉框3')

    def click_shuchu1(self):
        self.move_click(self.jishuanzujuan1,68,17)
        Logger().info('查看碰撞求同输出框')

    def click_big1(self):
        self.click(self.big1)
        Logger().info('点击输出框缩放按钮')

    def click_small1(self):
        self.click(self.small1)
        Logger().info('点击输出框缩放按钮')

    def type_search1(self,text):
        self.type(self.search1,text)
        Logger().info('搜索框输入')

    def click_ziduan1(self):
        self.click(self.ziduan1)
        Logger().info('勾选输出字段1')

    def click_ziduan_1(self):
        self.click(self.ziduan_1)
        Logger().info('勾选右侧输出字段1')

    def click_shuchu_1(self):
        self.click(self.shuchu_1)
        Logger().info('点击输出')

    def click_chehui_1(self):
        self.acclick(self.chehui_1)
        Logger().info('点击撤回')

    '''
    数据源2
    '''
    def click_shujuyuan2(self):
        self.click(self.shujuyuan2)
        Logger().info('打开数据源2环形菜单')

    def click_shuchu2(self):
        self.click(self.shuchu2)
        Logger().info('查看数据源2输出框')

    def click_delete2(self):
        self.move_click(self.shujuyuan2, -34, 0)
        Logger().info('删除数据源2')

    def click_choose_all2(self):
        self.click(self.choose_all2)
        Logger().info('数据源2输出框左侧全选')

    def click_choose_lla2(self):
        self.click(self.choose_lla2)
        Logger().info('数据源2输出框右侧全选')

    def click_shuchu_2(self):
        self.click(self.shuchu_2)
        Logger().info('数据源2输出框向右输出')

    def click_chehui_2(self):
        self.click(self.chehui_2)
        Logger().info('数据源2输出框向左撤回')

    '''
    数据源3
    '''
    def click_shujuyuan3(self):
        self.click(self.shujuyuan3)
        Logger().info('打开数据源3环形菜单')

    def click_delete3(self):
        self.move_click(self.shujuyuan3, -34, 0)
        Logger().info('删除数据源3')

    '''
    二级连接
    '''
    jishuanzujuan5 = 'x=>//*[@id="ioper_02_5"]'
    peizhi5 = 'x=>//*[@id="menu0_5"]'
    peizhi5_1 = 'x=>//*[@id="ioper_02_5_a"]/div/div[1]/div/div[1]/input'
    peizhi5_12 = 'x=>/html/body/div[2]/div[1]/div[1]/ul/li[2]'
    peizhi1_12 = 'x=>/html/body/div[2]/div[1]/div[1]/ul/li[2]'

    def click_peizhi1_12(self):
        self.click(self.peizhi1_12)
        Logger().info('选择通关时间')

    def click_jishuanzujian5(self):
        self.click(self.jishuanzujuan5)
        Logger().info('点击计算组件5')

    def click_peizhi5(self):
        self.move_click(self.jishuanzujuan5, 34, -20)
        Logger().info('点击组件5配置')

    def click_peizhi5_list(self):
        self.click(self.peizhi5_1)
        Logger().info('选择通关时间字段')

    def click_peizhi5_12(self):
        self.click(self.peizhi5_12)
        Logger().info('选择通关时间字段')

    def click_peizhi5_1(self):
        self.click(self.peizhi5_1)
        Logger().info('点击下拉框1')






























