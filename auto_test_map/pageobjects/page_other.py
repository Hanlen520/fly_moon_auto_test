# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 0024 9:21
# @Author  : 郝一阳
# @FileName: page_other.py
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

#眉页菜单
class Other(BasePage):
    '''***
    公有部分
    ***'''
    model = 'xpath=>//*[@id="tab-model"]'
    run = 'xpath=>/html/body/div/div[2]/nav/ul/li[4]/a'
    public_model = 'x=>//*[@id="pane-model"]/ul/li[1]/span'

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

    filter_model1 = 'x=>//*[@id="pane-model"]/div[2]/ul[1]/li[31]'

    def double_model1(self):
        time.sleep(1)
        self.click_twice(self.filter_model1)
        Logger().info('进入同wifi模型1(单数据源)')

    """*********
    *********"""

    data_search1 = 'x=>//*[@id="pane-source"]/div[1]/input'
    public_data1 = 'x=>//*[@id="node_1015"]/span'
    model_search1 = 'x=>//*[@id="pane-model"]/div[1]/input'
    self_model1 = 'x=>//*[@id="pane-model"]/div[2]/ul[1]/li[1]/a'

    def type_data_search1(self,text):    #重
        self.type(self.data_search1,text)
        Logger().info('公有资源搜索%d' %text)

    def compair_public_data1(self,text):   #旅客重点人
        self.findtext(self.public_data1,text)
        Logger().info('搜索结果为%d' %text)

    def type_model_search1(self,text):  #异
        self.type(self.model_search1,text)
        Logger().info('自有模型搜索%d' %text)

    def compair_self_model1(self,text):
        self.findtext(self.self_model1,text)
        Logger().info('搜索结果为%d' %text)

    edit = 'x=>//*[@id="pane-model"]/div[2]/ul[1]/li[47]/span/button/span'
    edit_name = 'x=>//*[@id="#modals-container"]/div/div/div[2]/div/div[2]/form/div[1]/div/div/input'
    confirm = 'x=>//*[@id="#modals-container"]/div/div/div[2]/div/div[2]/form/div[3]/button[1]'
    reset = 'x=>//*[@id="#modals-container"]/div/div/div[2]/div/div[2]/form/div[3]/button[2]'
    delete = 'x=>//*[@id="el-popover-6906"]/button[3]'
    save = 'x=>//*[@id="app"]/div[2]/nav/ul/li[2]/a'
    osave = 'x=>//*[@id="app"]/div[2]/nav/ul/li[3]/a'

    def click_edit(self):
        self.click(self.edit)
        Logger().info('点击编辑')

    def type_edit_name(self):
        self.type(self.edit_name,'编辑1')

    def click_confirm(self):
        self.click(self.confirm)
        Logger().info('点击确认')

    def click_delete(self):
        self.click(self.delete)
        Logger().info('点击删除')

    def click_save(self):
        self.click(self.save)
        Logger().info('点击保存')

    def click_osave(self):
        self.click(self.osave)
        Logger().info('点击另存')



































