from django.shortcuts import render
from .models import Product
# Create your views here.

def current_product(request, slug):
    template = 'current_product.html'
    current_product = Product.objects.get(slug=slug)
    ctx = {
    'current_product': current_product,    
    }
    return render(request, template, ctx)