from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView, ZipCodeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'politics.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<zipcode>[0-9]{5})/$', ZipCodeView.as_view(), name='zip-detail'),
)
