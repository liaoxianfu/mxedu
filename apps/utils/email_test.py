# encoding: utf-8
import email

__author__ = 'liaoxianfu'
__date__ = '2018/10/28 11:27'

from email.mime.text import MIMEText

import smtplib
import email.mime.multipart
import email.mime.text


def email_send(mail_host, mail_user, password, sender, receiver, subject, content):
    """
    发送邮件 使用本地的ip可能会失败
    :param mail_host: smtp的主机 例如 163的smtp.163.com
    :param mail_user: 邮箱账户 例如 xx@163.com
    :param password: 邮箱密码或者授权码 一般现在会要求使用授权码进行第三方的登录
    :param sender: 发送者 一般与mail_user相同即可
    :param receiver: 接受者 接受邮件的用户邮箱
    :param subject: 主题名称
    :param content: 邮件内容
    :return: 是否发送成功
    """
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 994)
        smtpObj.login(mail_user, password)
        smtpObj.sendmail(sender, receiver, msg.as_string())
        smtpObj.quit()
        return True
    except smtplib.SMTPException as e:
        return False


def send_email():
    # coding:utf-8

    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "15236735895@163.com"  # 用户名
    mail_pass = "liao1234"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

    sender = '15236735895@163.com'
    receivers = ['liaoxianfu555@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    msg = email.mime.multipart.MIMEMultipart()
    '''
    最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因
    '''
    msg['Subject'] = '加油'
    msg['From'] = sender
    msg['To'] = receivers[0]
    content = '''''
        你好，
        数据一斤收到
    '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 994)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers[0], msg.as_string())
        smtpObj.quit()
        print(u"邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    send_email()
