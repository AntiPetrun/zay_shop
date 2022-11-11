from homepage.views import ContextMixin
from django.views.generic import ListView, DetailView
from .models import Product, Category
from cookbook.models import Brand
from django.db.models import Q
from django.shortcuts import render


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


class ProductListView(ShopMixin, GetValuesForFilters, ListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self):
        context = super(ProductListView, self).get_context_data()
        context.update(self.context)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        context.update({
            'categories': categories,
            'brands': brands,
        })
        context['user_profile'] = self.request.user
        return context


class GenderProductListView(ProductListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'
    object_list = None

    def get(self, request, gender):
        context = self.get_context_data()
        context[self.context_object_name] = Product.objects.filter(gender=gender)
        return render(request, self.template_name, context)


class CategoryProductListView(ProductListView):
    template_name = 'catalog/shop.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True).filter(category__slug=self.kwargs['cat_slug'])


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
        context['user_profile'] = self.request.user
        return context
