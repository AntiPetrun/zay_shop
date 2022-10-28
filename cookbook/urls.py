from django.urls import path
from .views import index

app_name = 'cookbook'

urlpatterns = [
    path('', index, name='about'),
]
