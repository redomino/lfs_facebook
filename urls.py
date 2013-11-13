try:
    from django.conf.urls import patterns, url, include
except ImportError:
    from django.conf.urls.defaults import patterns, url, include

from lfs_facebook import views

urlpatterns = patterns('',
    url(r'^login', views.login, name='login'),    
)
