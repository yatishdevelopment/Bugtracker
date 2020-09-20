
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import  url
import bugapp
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^employee/$', views.employee, name='employee'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^add_bug/$', views.add_bug, name='add_bug'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^all_projects/$', views.all_projects, name='all_projects'),
    url(r'^issue_by_user/(\d+)/$', views.issue_by_user, name='issue_by_user'),
    url(r'^issue_edit/$', views.issue_edit, name='issue_edit'),
    url(r'^issue_stats/(?P<status>[\w\-]+)/$', views.issue_stats, name='issue_stats'),

    url(r'^issue_edit/(\d+)/$', views.issue_edit, name='issue_edit'),

]