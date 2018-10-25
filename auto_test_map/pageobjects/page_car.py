# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 0016 11:10
# @Author  : 郝一阳
# @FileName: page_car.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2018/7/12 0012 14:21
# @Author  : 郝一阳
# @FileName: page_locus.py
# @Software: PyCharm
# coding=utf-8
from public.base_page import BasePage
from public.logger import Logger
import time
import selenium.webdriver.support.ui as ui
from public.browser_engine import BrowserEngine
from public.logger import Logger
import os,sys,time
from selenium.webdriver.support import expected_conditions as EC

#同车随行
class Car(BasePage):
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



    '''*******
    同车随行模型
    *******'''
    filter_model1 = 'x=>//*[@id="pane-model"]/div[2]/ul[1]/li[3]'
    filter_model2 = 'x=>//*[@id="pane-model"]/div[2]/ul[1]/li[2]'
    filter_model3 = 'x=>//*[@id="pane-model"]/div[2]/ul[1]/li[1]'

    def double_model1(self):
        time.sleep(1)
        self.click_twice(self.filter_model1)
        Logger().info('进入同车随行模型1(单数据源)')

    def double_model2(self):
        time.sleep(1)
        self.click_twice(self.filter_model2)
        Logger().info('进入同车随行模型2（双组件）')

    def double_model3(self):
        time.sleep(1)
        self.click_twice(self.filter_model3)
        Logger().info('进入同车随行模型3（多数据源）')

    def double_model4(self):
        time.sleep(1)
        self.click_twice(self.filter_model4)
        Logger().info('进入同车随行模型4（连接同车随行组件）')

    def double_model5(self):
        time.sleep(1)
        self.click_twice(self.filter_model5)
        Logger().info('进入同车随行模型5（连接其它组件）')

    """*********
    连接两个数据源
    *********"""
    jishuanzujuan1 = 'x=>//*[@id="ioper_15_1"]'
    preview1 = 'x=>//*[@id="menu3_1"]'  #预览
    preview1now = 'x=>//*[@id="ioper_15_1_c"]/button'    #当前结果
    delete1 = 'x=>//*[@id="menu3_undefined"]'
    peizhi1 = 'x=>//*[@id="menu0_undefined"]'
    shuchu1 = 'x=>//*[@id="menu1_undefined"]'
    ziduan1 = 'x=>//*[@id="ioper_15_1_b"]/div/div[1]/div[3]/label[1]'
    ziduan_1 = 'x=>//*[@id="ioper_15_1_b"]/div/div[3]/div/label/span[2]'
    shuchu_1 = 'x=>//*[@id="ioper_15_1_b"]/div/div[2]/button[1]/i'
    chehui_1 = 'x=>//*[@id="ioper_15_1_b"]/div/div[2]/button[2]/i'
    search1 = 'x=>//*[@id="ioper_15_1_a"]/div[2]/div[1]/div[1]/input'
    choose_all1 = 'x=>//*[@id="ioper_15_1_a"]/div[2]/div[1]/label/span[1]'
    choose_lla1 = 'x=>//*[@id="ioper_15_1_a"]/div[2]/div[3]/label/span[1]/span'
    peizhi1_5 = 'x=>//*[@id="ioper_15_1_a"]/div[3]/div[2]/div/div[1]/input'
    peizhi1_7 = 'x=>//*[@id="ioper_15_1_a"]/div[2]/div/div[1]/div/div[1]/input'
    peizhi1_8 = 'x=>//*[@id="ioper_15_1_a"]/div[4]/div[3]/div/div[1]/input'

    shujuyuan2 = 'x=>//*[@id="cnode_1039_2"]'
    delete2 = 'x=>//*[@id="menu6_undefined"]'
    shuchu2 = 'x=>//*[@id="menu2_undefined"]'
    ziduan2 = 'x=>//*[@id="cnode_1039_2_b"]/div/div[1]/div[3]/label[1]/span[2]'
    ziduan_2 = 'x=>//*[@id="cnode_1039_2_b"]/div/div[3]/div[2]/label[1]/span[2]'
    choose_all2 = 'x=>//*[@id="cnode_1039_2_b"]/div/div[1]/label/span[1]/span'
    choose_lla2 = 'x=>//*[@id="cnode_1039_2_b"]/div/div[3]/label/span[1]/span'
    shuchu_2 = 'x=>//*[@id="cnode_1039_2_b"]/div/div[2]/button[1]/i'
    chehui_2 = 'x=>//*[@id="cnode_1039_2_b"]/div/div[2]/button[2]/i'

    shujuyuan3 = 'x=>//*[@id="cnode_1036_3"]'
    delete3 = 'x=>//*[@id="menu5_3"]'

    jishuanzujuan3 = 'x=>//*[@id="ioper_11_3"]'




    '''
    同车随行1
    '''
    def click_jishuanzujian1(self):
        self.click(self.jishuanzujuan1)
        Logger().info('打开同车随行组件的环形菜单')

    def click_preview1(self):
        self.move_click(self.jishuanzujuan1,0,68)
        Logger().info('点击预览')

    def click_preview1now(self):
        self.click(self.preview1now)
        Logger().info('预览计算')

    def click_delete1(self):
        self.move_click(self.jishuanzujuan1, -34,0)
        Logger().info('点击删除')

    def click_choose_lla1(self):
        self.click(self.choose_lla1)
        Logger().info('右侧全选')

    def click_peizhi1(self):
        self.move_click(self.jishuanzujuan1,34,-20)
        Logger().info('查看同车随行配置框')


    def click_peizhi1_1(self):
        self.click(self.peizhi1_1)
        Logger().info('查看配置下拉框1')

    def compair_peizhi1_1(self, name):
        self.findtext(self.peizhi1_1 ,name)
        #assert mes == u'%s' % txt
        Logger().info('对比搜索字段')

    def compair_ziduan1(self, name):
        self.findtext(self.ziduan1,name)

    def click_peizhi1_2(self):
        self.click(self.peizhi1_2)
        time.sleep(1)
        Logger().info('查看配置下拉框3')

    def click_shuchu1(self):
        self.move_click(self.jishuanzujuan1,68,17)
        Logger().info('查看同车随行输出框')

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
        self.click_shuchu(self.search1)
        Logger().info('点击输出')

    def click_chehui_1(self):
        self.click_chehui(self.search1)
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
    jishuanzujuan5 = 'x=>//*[@id="ioper_05_4"]'
    peizhi5 = 'x=>//*[@id="menu0_5"]'
    peizhi5_1 = 'x=>//*[@id="ioper_03_5_a"]/div/div[1]/div/div[1]/input'

    def click_peizhi1_22(self):
        self.move_click(self.peizhi1_2,70,74)
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

    peizhi1_3 = 'x=>//*[@id="ioper_15_1_a"]/div/div[2]/div[4]/div/input'
    peizhi1_2 = 'x=>//*[@id="ioper_15_1_a"]/div/div[2]/div/div/input'
    peizhi1_1 = 'x=>//*[@id="ioper_15_1_a"]/div[1]/div[1]/div[1]/div/div[1]/input'
    peizhi1_13 = 'x=>/html/body/div[4]/div[1]/div[1]/ul/li[3]'
    peizhi1_21 = 'x=>/html/body/div[4]/div[1]/div[1]/ul/li[1]'
    peizhi1_12 = 'x=>/html/body/div[2]/div[1]/div[1]/ul/li[2]'

    def click_peizhi1_13(self):
        self.move_click(self.peizhi1_1,80,110)
        Logger().info('选择卡口字段')

    def click_peizhi1_21(self):
        self.move_click(self.peizhi1_2,80,45)
        Logger().info('选择关系包含')

    def type_peizhi1_3(self,text):
        self.type(self.peizhi1_3,text)
        Logger().info('选择关系包含')

    def click_peizhi1_12(self):
        self.select2(self.peizhi1_1)
        Logger().info('选择下拉框2')

    def click_peizhi1_11(self):
        self.select1(self.peizhi1_1)
        Logger().info('选择下拉框1')

    clean1 = 'x=>//*[@id="ioper_15_1_a"]/div/div[2]/div[5]/button[2]'
    zheng = 'x=>//*[@id="ioper_15_1_a"]/div/div[2]/div[5]/button[1]'
    peizhi1_6 = 'x=>//*[@id="ioper_15_1_a"]/div[1]/div[3]/div[3]/div/input'


    def type_peizhi1_6(self,text):
        self.type(self.peizhi1_6,text)
        Logger().info('搜索框输入%s'%text)

    def click_peizhi1_7(self):
        self.click(self.peizhi1_7)
        Logger().info('点击配置框7')

    def click_peizhi1_71(self):
        self.select1(self.peizhi1_7)

    def click_jishuanzhujian3(self):
        self.click(self.jishuanzujuan3)
        Logger().info('点击计算组件3')

    def click_shuchu3(self):
        self.move_click(self.jishuanzujuan3,68,17)
        Logger().info('查看同车随行输出框')

    def click_peizhi3(self):
        self.move_click(self.jishuanzujuan3,34,-20)
        Logger().info('查看同车随行配置框')

    def click_shuchu5(self):
        self.ji_shuchu(self.jishuanzujuan5)
        Logger().info('组件5输出框')

    ziduan4_1 = 'x=>//*[@id="ioper_05_4_b"]/div/div[1]/div[3]/label[2]/span[2]'
    def compair_ziduan4_1(self,text):
        self.findtext(self.ziduan4_1,text)































