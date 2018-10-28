# encoding: utf-8
from django.template import loader

__author__ = 'liaoxianfu'
__date__ = '2018/10/28 9:39'

from random import Random
from users.models import EmailVerifyRecord
from email.mime.text import MIMEText
import smtplib
import email.mime.multipart
import email.mime.text

from mxedu.settings import MAIL_HOST, MAIL_PASS, MAIL_USER, SENDER


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
        print(e)
        return False


def random_str(str_len):
    """
    发送随机字符串
    :return:
    """

    ran_str = ''
    all_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(all_chars) - 1
    random = Random()
    for i in range(str_len):
        ran_index = random.randint(0, length)
        ran_str += all_chars[ran_index]

    return ran_str


def send_email(email, send_type="register"):
    """
    发送Email邮件 并在数据库中保存相应的数据\n
    :param email:
    :param send_type:
    :return:
    """
    email_record = EmailVerifyRecord()
    code = random_str(str_len=16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # 定义邮件内容:
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}/{1}".format(email, code)

        send_status = email_send(mail_host=MAIL_HOST, mail_user=MAIL_USER, password=MAIL_PASS, sender=MAIL_USER,
                                 receiver=email, subject=email_title, content=email_body)
        # 如果发送成功
        if send_status:
            print("成功")
        else:
            print("失败")

    elif send_type == "forget":
        email_title = "找回密码链接"
        email_body = "请点击下面的链接重置密码: http://127.0.0.1:8000/reset_pass/{0}/{1}".format(email, code)

        send_status = email_send(mail_host=MAIL_HOST, mail_user=MAIL_USER, password=MAIL_PASS, sender=MAIL_USER,
                                 receiver=email, subject=email_title, content=email_body)
        if send_status:
            print("成功")
        else:
            print("失败")
    else:
        pass
