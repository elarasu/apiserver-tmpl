from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework import routers

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('hello.urls')),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r"^account/", include('account.urls')),
    url(r'^api/auth/', include('djoser.urls')),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
)
