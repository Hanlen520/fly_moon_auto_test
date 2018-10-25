# coding:utf-8

import os
#import smtplib
import time
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
from public.logger import Logger
import smtplib
from email.mime.text import MIMEText
#from email.header import Header
#from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

#from config import globalparam

# 测试报告的路径
report_path = os.path.dirname(os.path.abspath('.')) + '/testReport/'
logger = Logger()
# 收件人邮箱
receive_ddress = ['605865675@qq.com']
# 发件人邮箱
sender_address = 'haoyiyang@shuweitech.com'
sender_pswd = 'Hao87194962'


class SendMail:
    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = receive_ddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(report_path)
        dirs.sort()
        new_report_name = dirs[-1]
        print('The new report name: {0}'.format(new_report_name))
        return new_report_name

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        new_report = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '（自动邮件）脚本运行完毕，请查看报告'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(report_path, new_report), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sender_address
        try:
            smtp = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
            smtp.connect('smtp.exmail.qq.com')
            #smtp.starttls()
            smtp.login(sender_address, sender_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise



if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()