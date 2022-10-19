from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

from src.catalog.models import Product
from src.customer.models import AddressInfo, Customer

User = get_user_model()


class OrderStatus(models.Model):
    order = models.ForeignKey(
        'Order',
        _('Order Status'),
        on_delete=models.PROTECT,
        related_name='orders',
    )
    STATUS_CHOICES = (
        ('o', 'Open'),
        ('a', 'Archived'),
        ('c', 'Canceled')
    )
    status = models.CharField(
        _('Status'),
        choices=STATUS_CHOICES,
        max_length=64,
        default='o'
    )

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'order_status'
        verbose_name = _('Status')
        verbose_name_plural = _('Status')
        ordering = ('status',)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        _('Customer'),
        on_delete=models.SET_NULL,
        null=True,
        related_name='customers'
    )
    status = models.ForeignKey(
        'orders.Status',
        _('Order Status'),
        on_delete=models.DO_NOTHING,
        related_name='status',
    )
    delivery_address = models.ForeignKey(
        AddressInfo,
        _('Delivery Address Information'),
        on_delete=models.CASCADE,
        related_name='addresses',
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    @property
    def total_amount(self):
        total = 0
        for product in self.products.all():
            total += product.price
        return total

    def __str__(self):
        return f'{self.pk}: {self.customer}, {self.created_date},' \
               f'{self.status}, {self.total_amount}, {self.delivery_address}'

    class Meta:
        db_table = 'order_orders'
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ('-created_date', 'order')


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    product = models.ForeignKey(
        Product,
        _('product'),
        on_delete=models.CASCADE,
        related_name='products'
    )

    @property
    def get_price(self, product_pk):
        price = 0
        for product in self.products.filter(pk=product_pk):
            price = product.price
        return price

    @property
    def get_quant(self, product_pk):
        quant = 0
        for product in self.products.filter(pk=product_pk):
            quant = product.quantity
        return quant

    def __str__(self):
        return f'{self.pk}: {self.order}, {self.product},' \
               f'{self.get_quant}, {self.get_price}'
