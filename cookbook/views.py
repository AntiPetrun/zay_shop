from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return render(request, 'cookbook/about.html')


def contact(request: HttpRequest):
    return render(request, 'cookbook/contact.html')
