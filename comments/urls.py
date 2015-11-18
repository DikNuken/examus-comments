# -*- coding: utf-8 -*-
from comments.views import CommentsListApiView, CommentApiView
from django.conf.urls import url

__author__ = 'Pavel Dik'

urlpatterns = [
    url(r'^(?P<comment_pk>\d+)/$', CommentsListApiView.as_view(), name='comments'),
    url(r'^$', CommentApiView.as_view(), name='comments')
]
