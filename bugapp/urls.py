"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    url(r'^issue_by_user/(?P<pk>\d+)/$', views.issue_by_user, name='issue_by_user'),
    url(r'^issue_edit/$', views.issue_edit, name='issue_edit'),

    url(r'^issue_edit/(?P<pk>\d+)/$', views.issue_edit, name='issue_edit'),

]