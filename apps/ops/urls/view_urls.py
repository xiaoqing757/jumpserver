# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals


from django.conf.urls import url
from .. import views

__all__ = ["urlpatterns"]

app_name = "ops"

urlpatterns = [
    # TResource Task url
    url(r'^task/$', views.TaskListView.as_view(), name='task-list'),
    url(r'^task/(?P<pk>[0-9a-zA-Z\-]{36})/$', views.TaskDetailView.as_view(), name='task-detail'),
    url(r'^task/(?P<pk>[0-9a-zA-Z\-]{36})/adhoc/$', views.TaskAdhocView.as_view(), name='task-adhoc'),
    url(r'^task/(?P<pk>[0-9a-zA-Z\-]{36})/history/$', views.TaskHistoryView.as_view(), name='task-history'),
    url(r'^task/(?P<pk>[0-9a-zA-Z\-]{36})/run/$', views.TaskRunView.as_view(), name='task-run'),
]