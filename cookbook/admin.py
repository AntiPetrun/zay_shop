from django.contrib import admin

from .models import Brand, Color, Size


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Enter brand name for search'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Enter color name for search'


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Enter size title for search'
