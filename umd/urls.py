from django.conf.urls import patterns, url
from umd import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<url_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<url_id>\d+)/modify/$', views.modify, name='modify'),
	url(r'^add/$', views.add, name='add'),
)