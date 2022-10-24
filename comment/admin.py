from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    empty_value_display = 'no data'
    list_display = (
        'author',
        'body',
        'date_created'
    )
    list_filter = ('date_created',)
    search_fields = ('body',)
    search_help_text = 'Enter keywords for search'
