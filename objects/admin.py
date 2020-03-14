from django.contrib import admin
from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    class Meta:
        model = Product


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = ['product', 'price_for_one', 'numb', 'total_price']
    class Meta:
        model = ProductInBasket


class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'total_price']
    class Meta:
        model = Order

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)
admin.site.register(Order, OrderAdmin)