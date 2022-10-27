from django.urls import path
from .views import index, shop

app_name = 'catalog'

urlpatterns = [
    path('', index, name='catalog'),
    path('shop', shop, name='shop'),
]
