from django.shortcuts import render
from django.http import HttpRequest


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
        'designed_by': 'https://templatemo.com/',
    }


def index(request: HttpRequest):
    context = ContextMixin.context
    return render(request, 'homepage/index.html', context=context)
