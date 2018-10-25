# encoding: utf-8
__author__ = 'liaoxianfu'
__date__ = '2018/10/23 21:27'

import xadmin

from .models import EmailVerifyRecord, Banner

"""
xadmin 的全局配置
"""

from xadmin import views


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "过不去的过去: 后台管理"
    site_footer = "过不去的过去"
    # 收起菜单
    menu_style = "accordion"


# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
