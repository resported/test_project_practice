from django.db import models
from django.urls import reverse

from django.db.models.signals import post_save


class Type(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title 


class Product(models.Model):
    title = models.CharField(max_length=38)
    price = models.PositiveIntegerField()
    type = models.ForeignKey(Type, default=False,  on_delete=models.PROTECT)
    active = models.BooleanField(default=False)
    men = models.BooleanField(default=False)
    woman = models.BooleanField(default=False)
    slug = models.SlugField(db_index=True, primary_key=True, allow_unicode=True, unique=True, default=False)


    def current_product(self):
        return reverse('current_product', args=[str(self.slug)])

    def __str__(self):
        return self.title


class ProductInBasket(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, default=False, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_for_one = models.PositiveIntegerField(default=0, blank=True)
    numb = models.PositiveIntegerField(default=1, blank=True)
    total_price = models.PositiveIntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        product_price = self.product.price
        self.price_for_one = product_price
        self.total_price = self.numb * self.price_for_one

        super(ProductInBasket, self).save(*args, **kwargs)


class Order(models.Model):
    title = models.CharField(max_length=28)
    phone = models.PositiveIntegerField(blank=True, default=0)
    addres = models.CharField(max_length=128, blank=True)
    total_price = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.title


def order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    order.total_price = 0

    all_products_in_order = ProductInBasket.objects.filter(order=order)

    for item in all_products_in_order:
        order.total_price += item.total_price

    instance.order.total_price = order.total_price
    instance.order.save(force_update=True)

post_save.connect(order_post_save, sender=ProductInBasket)