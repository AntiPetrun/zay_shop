from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from .models import Comment


def index(request: HttpRequest):
    return HttpResponse('<h1>Comment</h1>')
