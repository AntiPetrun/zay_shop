from django.contrib import admin

from .models import Customer, AddressInfo, Feedback


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'customer',
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


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date_created',
    )
    list_filter = ('email', 'date_created',)
    search_fields = ('email',)
    search_help_text = 'Enter email for search'
