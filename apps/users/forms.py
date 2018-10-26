# encoding: utf-8
from django import forms

__author__ = 'liaoxianfu'
__date__ = '2018/10/26 17:27'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)
