from django.contrib import admin

from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'title',
        'subtitle',
    )
    list_filter = ('id',)
    search_fields = ('title', 'subtitle', 'id')
    search_help_text = 'Enter title, subtitle or id for search'
