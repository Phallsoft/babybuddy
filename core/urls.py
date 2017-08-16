# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'child/add/$', views.ChildAdd.as_view(), name='child-add'),
    url(r'child/(?P<pk>[0-9]+)/$', views.ChildUpdate.as_view(),
        name='child-update'),
    url(r'child/(?P<pk>[0-9]+)/delete/$', views.ChildDelete.as_view(),
        name='child-delete'),
]
