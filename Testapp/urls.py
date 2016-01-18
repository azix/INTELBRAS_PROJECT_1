# from django.conf.urls import patterns, url
from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *


urlpatterns = patterns('Testapp.views',
                       url(r'^$', 'index', {'template_name': 'Testapp/index.html'}, 'Testapp_home'),
                       url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', {
                               'template_name': 'Testapp/category.html'}, 'Testapp_category'),
                       url(r'^product/(?P<product_slug>[-\w]+)/$',
                           'show_product', {
                               'template_name': 'Testapp/product.html'}, 'Testapp_product'),
                       # url(r'^cart/', include('thecart.urls')),
                       )
