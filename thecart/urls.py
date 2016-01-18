from django.conf.urls import patterns, include, url

urlpatterns = patterns('thecart.views',
                       url(r'^$', 'show_cart', {'template_name': 'thecart/cart.html'}, 'show_cart'),
                       )
