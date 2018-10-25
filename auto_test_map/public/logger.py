#_*_ coding: utf-8 _*_
import logging
import os.path
import time
#
# class Logger(object):
#
#     def __init__(self, logger):
#         '''
#             指定保存日志的文件路径，日志级别，以及调用文件
#             将日志存入到指定的文件中
#         '''
#
#         # 创建一个logger
#         self.logger = logging.getLogger(logger)
#         self.logger.setLevel(logging.DEBUG)
#
#         # 创建一个handler，用于写入日志文件
#         rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
#         log_path = os.path.dirname(os.getcwd()) + '/Logs/'  # 项目根目录下/Logs 保存日志
#         #log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
#         # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
#         log_name = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
#         #log_name = log_path + rq + '.log'
#         fh = logging.FileHandler(log_name)
#         fh.setLevel(logging.INFO)
#
#         # 再创建一个handler，用于输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.INFO)
#
#         # 定义handler的输出格式
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         fh.setFormatter(formatter)
#         ch.setFormatter(formatter)
#
#         # 给logger添加handler
#         self.logger.addHandler(fh)
#         self.logger.addHandler(ch)
#
#
#     def getlog(self):
#         return self.logger
#coding=utf-8

import logging
import time
import os
#from config import globalparam

log_path = os.path.dirname(os.getcwd()) + '/logs/'
class Logger:
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self,message):
        self.__printconsole('debug', message)

    def info(self,message):
        self.__printconsole('info', message)

    def warning(self,message):
        self.__printconsole('warning', message)

    def error(self,message):
        self.__printconsole('error', message)
