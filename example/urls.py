# -*- coding: utf-8 -*-

from django.conf.urls import url
from example.views import ExampleView

__author__ = 'Pavel Dik'
urlpatterns = [
    url(r'^$', ExampleView.as_view())
]
