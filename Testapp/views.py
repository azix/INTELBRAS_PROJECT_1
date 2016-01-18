from django.shortcuts import get_object_or_404, render_to_response
from Testapp.models import Category, Product
from django.template import RequestContext
# this stuff goes at the top of the file, below other imports
from django.core import urlresolvers
from thecart import cart
from django.http import HttpResponseRedirect
from Testapp.forms import ProductAddToCartForm


def index(request, template_name="Testapp/index.html"):
    page_title = 'Supermarkets'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def show_category(request, category_slug, template_name="Testapp/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))


def show_product(request, product_slug, template_name="Testapp/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))
