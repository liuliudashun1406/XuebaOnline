"""XuebaOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

from accounts import urls as accounts_urls
from stackExchange import urls as crawl_urls
from question import urls as question_urls

urlpatterns = [
    url(r'^new/$',views.static_page,{'template_name':'xuebaonline.html'}),
    url(r'^/{0,1}$',views.index),
    url(r'^index/$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^crawler/', include(crawl_urls)),
    url(r'^display/$', views.test_display_meta),
    url(r'^search/query/$', views.query),
    url(r'^feedback/$', views.feedback),
    url(r'^robot/$', views.robot),
    url(r'^robot/contact', views.robot_contact, name='robot_contact'),
    url(r'^course/$', views.course),
    url(r'^course/compiler/$', views.courseCompiler),
    url(r'^question/', include(question_urls)),
]
