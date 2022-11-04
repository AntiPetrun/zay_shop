from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from homepage.views import ContextMixin


def index(request: HttpRequest):
    context = ContextMixin.context
    return render(request, 'catalog/shop-single.html', context=context)


def shop(request: HttpRequest):
    context = ContextMixin.context
    return render(request, 'catalog/shop.html', context=context)
