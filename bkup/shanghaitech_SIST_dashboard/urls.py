"""shanghaitech_SIST_dashboard URL Configuration

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
from django.views.generic import TemplateView
from shanghaitech_SIST_dashboard.views import datacontrol

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="dashboard/dashboard.html")),
    url(r'^datacontrol/$', datacontrol),
    url(r'^nodes/$', TemplateView.as_view(template_name="dashboard/nodes.html")),
    url(r'^templates/$', TemplateView.as_view(template_name="dashboard/dashboard.html")),
    url(r'^status/$', TemplateView.as_view(template_name="dashboard/dashboard.html")),
    url(r'^settings/$', TemplateView.as_view(template_name="dashboard/dashboard.html")),
    url(r'^about/$', TemplateView.as_view(template_name="dashboard/dashboard.html")),
]
