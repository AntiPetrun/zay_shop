from django.views.generic import TemplateView
from catalog.models import Product, Category
from .models import Banner
from django.db.models import Q


class ContextMixin:
    context = {
        'site_title': 'Zay',
        'nav_home': 'Home',
        'nav_about': 'About',
        'nav_shop': 'Shop',
        'nav_contact': 'Contact',
        'shop_address': 'Svobody Street, 4, Minsk',
        'shop_email': 'info@zay.com',
        'shop_phone': '+375(33)-34-34-612',
        'facebook': 'https://facebook.com',
        'instagram': 'https://www.instagram.com/',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://www.linkedin.com/',
        'footer_nav_col1': 'Zay Shop',
        'footer_nav_col2': 'Products',
        'footer_nav_col3': 'Further Info',
    }


class HomeMixin(ContextMixin):
    context = ContextMixin.context
    context.update({
        'cat_blog': 'Categories of The Month',
        'featured_prod_blog': 'Featured Product',
    })


class HomeTemplateView(HomeMixin, TemplateView):
    template_name = 'homepage/index.html'
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeTemplateView, self).get_context_data()
        context.update(self.context)
        context['categories'] = Category.objects.all()
        context['month_cats'] = Category.objects.filter(
            Q(title__iexact="watches") |
            Q(title__iexact="casual shoes") |
            Q(title__iexact="sunglass")
        )
        context['banners'] = Banner.objects.all()
        context['products'] = Product.objects.order_by('-rating').filter(
            rating__gte=4
        )[:3]
        return context
