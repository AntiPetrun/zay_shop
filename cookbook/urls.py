from django.urls import path
from .views import index, contact

app_name = 'cookbook'

urlpatterns = [
    path('', index, name='about'),
    path('contact', contact, name='contact'),
]
