from django.urls import path
from .views import index, CatalogListView

app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='shop'),
    path('card', index, name='card'),
]
