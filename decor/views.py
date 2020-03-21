from django.shortcuts import render
from objects.models import *
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse

def main(request):
    template = 'basic/main.html'
    products = Product.objects.all()

    ctx = {
        'products': products,
    }
    
    return render(request, template, ctx)


def basket_adding(request):
    return_dict = dict()
    print(request.POST)

    return JsonResponse(return_dict)