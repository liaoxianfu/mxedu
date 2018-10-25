# encoding: utf-8

"""
注册地点，课程机构，教师的信息到django xadmin

"""

__author__ = 'liaoxianfu'
__date__ = '2018/10/24 8:32'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = [
        'name', 'desc', 'add_time'
    ]
    search_fields = [
        'name', 'desc', 'add_time'
    ]
    list_filter = [
        'name', 'desc', 'add_time'
    ]


xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = [
        'name', 'desc', 'click_nums', 'fav_nums', 'city'
    ]
    search_fields = [
        'name', 'desc', 'click_nums', 'fav_nums', 'city'
    ]
    list_filter = [
        'name', 'desc', 'click_nums', 'fav_nums', 'city__name'
    ]


xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = [
        'name', 'work_position', 'work_years', 'org'
    ]
    search_fields = [
        'name', 'work_position', 'work_years', 'org'
    ]
    list_filter = [
        'name', 'work_position', 'work_years', 'org__name'
    ]


xadmin.site.register(Teacher, TeacherAdmin)
