# coding=utf-8
from public import HTMLTestRunner
from testsuits.test_combine import Combine01
import os.path
import unittest
import time
from public import email_send


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/testReport/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 构建suite
# suite = unittest.TestSuite()
# suite.addTest(Combine01('test_combine_2b'))
#suite.addTest(Combine01('test_combine_1b2'))

test_dir = os.path.dirname(os.path.abspath('.')) + '/testsuits/'
suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')


if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"MAP公安大数据建模平台测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    # 发送邮件
    mail = email_send.SendMail()
    mail.send()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='cal_report',report_title='字段化测试报告'))
