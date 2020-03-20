from django.shortcuts import render
from objects.models import *


def main(request):
    template = 'basic/main.html'
    products = Product.objects.all()

    ctx = {
        'products': products,
    }
    
    return render(request, template, ctx)

