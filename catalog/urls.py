from django.urls import path
from .views import index, shop

app_name = 'catalog'

urlpatterns = [
    path('', shop, name='shop'),
    path('', index, name='card'),
]
