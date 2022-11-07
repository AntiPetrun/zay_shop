from django.shortcuts import render
from django.http import HttpRequest
from homepage.views import ContextMixin
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cookbook.models import Brand
from django.db.models import Q


class GetValuesForFilters:

    def get_featured_prods(self):
        return Product.objects.filter(rating__gte='4')

    def get_a_to_z(self):
        return Product.objects.all().order_by('name')

    def get_z_to_a(self):
        return Product.objects.all().order_by('-name')

    def get_low_to_high(self):
        return Product.objects.all().order_by('price')

    def get_high_to_low(self):
        return Product.objects.all().order_by('-price')


def index(request: HttpRequest):
    context = ContextMixin.context
    return render(request, 'catalog/shop-single.html', context=context)


class ShopMixin(ContextMixin):
    context = ContextMixin.context
    context.update({
        'cat_name': 'Categories',
    })


class ProdCardMixin(ContextMixin):
    context = ContextMixin.context
    context.update({
        'brand': 'Brand:',
        'descr': 'Description:',
        'color': 'Avaliable Color:',
        'specs': 'Specification:',
        'size': 'Size:',
        'quant': 'Quantity:',
        'related_prods': 'Related Products',
    })


class CatalogListView(ShopMixin, GetValuesForFilters, ListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self):
        context = super(CatalogListView, self).get_context_data()
        context.update(self.context)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        context.update({
            'categories': categories,
            'brands': brands,
        })
        return context


class MenCategoryListView(CatalogListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(gender__exact='1')


class WomenCategoryListView(CatalogListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self, *, object_list=None, **kwargs):
        return Product.objects.filter(gender__exact='2')


class UnisexCategoryListView(CatalogListView):
    template_name = 'catalog/shop.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(gender__exact='3')


class CategoryListView(CatalogListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True).filter(category=self.kwargs['cat_pk'])


class ProductDetailView(ProdCardMixin, DetailView):
    template_name = 'catalog/shop-single.html'
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'prod_slug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['prod_slug'])

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update(self.context)
        context['products'] = Product.objects.filter(
            is_published=True
        ).filter(
            Q(brand=self.kwargs['brand']) | Q(gender__exact=self.kwargs['gender'])
        )
        return context
