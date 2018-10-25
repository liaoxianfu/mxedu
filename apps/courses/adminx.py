# encoding: utf-8
import xadmin
from courses.models import Course, Lesson, Video, CourseResource

__author__ = 'liaoxianfu'
__date__ = '2018/10/23 21:50'


class CourseAdmin(object):
    list_display = [
        'name', 'desc', 'detail', 'degree', 'learn_times', 'students'
    ]
    search_fields = [
        'name', 'desc', 'detail', 'degree', 'students'
    ]
    list_filter = [
        'name', 'desc', 'detail', 'degree', 'learn_times', 'students'
    ]


xadmin.site.register(Course, CourseAdmin)


class LessonAdmin(object):
    list_display = [
        'course', 'name', 'add_time'
    ]
    search_fields = [
        'course', 'name'
    ]

    # __name代表使用外键中name字段
    list_filter = [
        'course__name', 'name', 'add_time'
    ]


xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = [
        'lesson', 'name', 'add_time'
    ]
    search_fields = [
        'lesson', 'name'
    ]
    list_filter = [
        'lesson', 'name', 'add_time'
    ]


xadmin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(object):
    list_display = [
        'course', 'name', 'download', 'add_time'
    ]
    search_fields = [
        'course', 'name', 'download'
    ]
    # __name代表使用外键中name字段
    list_filter = [
        'course__name', 'name', 'download', 'add_time'
    ]


xadmin.site.register(CourseResource, CourseResourceAdmin)
