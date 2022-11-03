from django.contrib import admin

from .models import OrderStatus, Basket, Order, OrderItem


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'order',
        'status',
    )
    list_filter = ('status',)
    search_fields = ('status',)
    search_help_text = 'Enter status for search'


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'id',
        'customer',
        'created_date',
        'updated_date',
    )
    list_filter = ('created_date', 'created_date',)
    search_fields = ('id',)
    search_help_text = 'Enter id for search'
    readonly_fields = ('created_date', 'updated_date')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'id',
        'basket',
        'order_status',
        'delivery_address',
        'created_date',
        'updated_date',
        'is_paid'
    )
    list_filter = ('order_status', 'updated_date', 'created_date', 'is_paid')
    search_fields = ('delivery_address',)
    search_help_text = 'Enter address name for search'
    readonly_fields = ('created_date', 'updated_date')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'basket',
        'order',
        'display_products',
        'quantity',
        'price',
    )
    list_filter = ('price',)
    search_fields = ('display_products',)
    search_help_text = 'Enter product title for search'
