from django.conf.urls import patterns, url
from umd import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<url_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<url_id>\d+)/modify/$', views.modify, name='modify'),
	url(r'^add/$', views.add, name='add'),
	
	url(r'^add_url/$', views.add_url, name='add_url'),

)

'''
url(r'^(?P<url_id>\d+)/add_url/$', views.add_url, name='add_url'), -- this has to be given when url_id also is passsed right?
'''