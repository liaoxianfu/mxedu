# encoding: utf-8
import xadmin

__author__ = 'liaoxianfu'
__date__ = '2018/10/25 17:02'

from .models import *


class UserAskAdmin(object):
    list_display = [
        'name', 'mobile', 'course_name', 'add_time'
    ]
    search_fields = [
        'name', 'mobile', 'course_name', 'add_time'
    ]
    list_filter = [
        'name', 'mobile', 'course_name', 'add_time'
    ]


xadmin.site.register(UserAsk, UserAskAdmin)


class CourseCommentsAdmin(object):
    list_display = [
        'course', 'user', 'add_time'
    ]
    search_fields = [
        'course', 'user', 'add_time'
    ]
    list_filter = [
        'course__name', 'user__username', 'add_time'
    ]


xadmin.site.register(CourseComments, CourseCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = [
        'user', 'fav_id', 'fav_type', 'add_time'
    ]
    search_fields = [
        'user', 'fav_id', 'fav_type', 'add_time'
    ]
    list_filter = [
        'user__username', 'fav_id', 'fav_type', 'add_time'
    ]


xadmin.site.register(UserFavorite, UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = [
        'user', 'has_read', 'message', 'add_time'
    ]
    search_fields = [
        'user', 'has_read', 'message', 'add_time'
    ]
    list_filter = [
        'user', 'has_read', 'message', 'add_time'
    ]


xadmin.site.register(UserMessage, UserMessageAdmin)


class UserCourseAdmin(object):
    list_display = [
        'user', 'course', 'add_time'
    ]
    search_fields = [
        'user', 'course', 'add_time'
    ]
    list_filter = [
        'user__username', 'course__name', 'add_time'
    ]


xadmin.site.register(UserCourse, UserCourseAdmin)
