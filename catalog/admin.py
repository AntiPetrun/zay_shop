from django.contrib import admin
from .models import Category, Product


@admin.action(description='Publish')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Not publish')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=True)


class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    empty_value_display = 'no data'
    list_display = (
        'title',
        'parent',
        'description',
        'is_published'
    )
    list_filter = ('is_published',)
    search_fields = ('title', 'id')
    search_help_text = 'Enter title or id for search'
    inlines = (ProductTabularInline, )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = (make_published, make_unpublished)
    empty_value_display = 'no data'
    list_display = (
        'article',
        'title',
        'category',
        'price',
        'rating',
        'brand',
        'display_colors',
        'display_sizes',
        'is_published'
    )
    list_filter = ('category', 'brand', 'rating', 'is_published')
    search_fields = ('title', 'brand')
    search_help_text = 'Enter title and brand for search'
    date_hierarchy = 'date_published'
    fieldsets = (
        ('Main settings', {
            'fields': ('article', 'category', 'image', 'title', 'price', 'rating')
        }),
        ('Additional settings', {
            'fields': ('brand', 'description', 'colors', 'specification', 'sizes',
                       'date_created', 'date_published', 'is_published', 'slug')
        })
    )
    list_editable = ('category', 'is_published', 'price')
    prepopulated_fields = {
        'slug': ('title', 'category',)
    }
    readonly_fields = ('rating', 'date_created', 'date_published')
