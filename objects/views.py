from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore

from .models import Product
# Create your views here.

def current_product(request, slug):
    template = 'current_product.html'
    current_product = Product.objects.get(slug=slug)
    ctx = {
    'current_product': current_product,  
    }

    request.session.set_test_cookie()

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        return render(request, template, ctx)
    else:
        return 'Set cookie!'


