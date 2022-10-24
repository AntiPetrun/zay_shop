from django.contrib import admin

from .models import Customer, AddressInfo


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'last_name',
        'first_name',
        'phone',
        'email',
    )
    list_filter = ('last_name', 'first_name',)
    search_fields = ('last_name', 'first_name',)
    search_help_text = 'Enter last or first name for search'


@admin.register(AddressInfo)
class AddressInfoAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'customer',
        'contact_name',
        'city',
        'street',
        'building',
        'room',
    )
    list_filter = ('customer', 'city',)
    search_fields = ('city',)
    search_help_text = 'Enter city name for search'
