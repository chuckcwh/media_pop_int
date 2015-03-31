from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'media_pop_app.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),

    # ajax call
    url(r'^keySet/$', 'media_pop_app.views.keySet', name='keySet'),
    url(r'^getKeys/$', 'media_pop_app.views.getKeys', name='getKeys'),

)
