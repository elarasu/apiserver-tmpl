from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/auth/', include('djoser.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
)
