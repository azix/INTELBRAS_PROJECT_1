from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^', include('catalog.urls')),
                       # url(r'^cart/', include('cart.urls')),
                       # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                       #     {'document_root': '/home/Documents/projecttest/static'}),
                       # (r'^Testapp/$', 'preview.views.home'),
                       url(r'^', include('Testapp.urls')),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': '/home/Documents/projecttest/Testapp/static'}),
                       # url(r'^cart/', include('thecart.urls')),
                       )


handler404 = 'Testapp.views.file_not_found_404'