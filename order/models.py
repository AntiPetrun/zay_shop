from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderStatus(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.PROTECT,
        related_name='orders',
    )
    STATUS_CHOICES = (
        ('o', 'Open'),
        ('a', 'Archived'),
        ('c', 'Canceled')
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=64,
        default='o'
    )

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'order_orders_status'
        verbose_name = _('Status')
        verbose_name_plural = _('Status')
        ordering = ('status',)


class Basket(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    created_date = models.DateField(
        auto_now_add=True
    )
    updated_date = models.DateField(
        auto_now=True
    )

    @property
    def total_amount(self):
        total = 0
        for product in self.products.all():
            total += product.price
        return total

    def __str__(self):
        return f'Customer: {self.customer}'


class Order(models.Model):
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        null=True,
        related_name='baskets'
    )
    order_status = models.ForeignKey(
        OrderStatus,
        on_delete=models.DO_NOTHING,
        related_name='order_status',
    )
    delivery_address = models.ForeignKey(
        'customer.AddressInfo',
        on_delete=models.CASCADE,
        related_name='addresses',
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.pk}: {self.bascket.customer},' \
               f'{self.basket.total_amount}, {self.order_status}'

    class Meta:
        db_table = 'order_orders'
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ('-created_date', 'order_status')


class OrderItem(models.Model):
    basket = models.ForeignKey(
        Basket,
        on_delete=models.SET_NULL,
        related_name='carts',
        null=True
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='goods'
    )
    products = models.ManyToManyField(
        'catalog.Product',
        related_name='products'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Quantity'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.basket}: {self.order},' \
               f'{self.quantity}, {self.price}'

    class Meta:
        db_table = 'order_order_items'
        verbose_name = _('order item')
        verbose_name_plural = _('order items')
