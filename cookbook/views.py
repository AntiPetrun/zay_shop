from django.views.generic import ListView
from .models import Brand
from homepage.views import ContextMixin
from catalog.models import Category


class AboutMixin(ContextMixin):
    context = ContextMixin.context
    context.update({
        'blog_service': 'Our Services',
        'blog_brands': 'Our Brands',
        'delivery': 'Delivery Services',
        'conditions': 'Shipping & Return',
        'promotion': 'Promotion',
        'call_center': '24 Hours Service',
    })


class BrandListView(AboutMixin, ListView):
    template_name = 'cookbook/about.html'
    model = Brand
    context_object_name = 'brands'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BrandListView, self).get_context_data()
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['user_profile'] = self.request.user
        return context
