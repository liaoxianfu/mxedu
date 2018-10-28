# encoding: utf-8
from captcha.fields import CaptchaField
from django import forms

__author__ = 'liaoxianfu'
__date__ = '2018/10/26 17:27'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致。
    email = forms.EmailField(required=True)
    # 密码不能小于5位
    password = forms.CharField(required=True, min_length=5)
    # 应用验证码
    captcha = CaptchaField()
