from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return render(request, 'catalog/shop-single.html')


def shop(request: HttpRequest):
    return render(request, 'catalog/shop.html')
