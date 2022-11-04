from django.shortcuts import render
from django.http import HttpRequest
from homepage.views import ContextMixin
from django.views.generic import ListView

from .models import Product, Category


def index(request: HttpRequest):
    context = ContextMixin.context
    return render(request, 'catalog/shop-single.html', context=context)


class ShopMixin(ContextMixin):
    context = ContextMixin.context
    context.update({
        'cat_name': 'Categories',
    })


class CatalogListView(ShopMixin, ListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self):
        context = super(CatalogListView, self).get_context_data()
        context.update(self.context)
        categories = Category.objects.all()
        context.update({
            'categories': categories,
            # 'subcategories': subcategories,
        })
        return context
