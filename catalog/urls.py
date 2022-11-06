from django.urls import path
from .views import index, CatalogListView, MenCategoryListView, \
    WomenCategoryListView, UnisexCategoryListView, CategoryListView

app_name = 'catalog'

urlpatterns = [
    path('', CatalogListView.as_view(), name='shop'),
    path('men', MenCategoryListView.as_view(), name='shop_men'),
    path('women', WomenCategoryListView.as_view(), name='shop_women'),
    path('unisex', UnisexCategoryListView.as_view(), name='shop_unisex'),
    path('category_products/<int:cat_pk>', CategoryListView.as_view(), name='cat_prods'),
    path('card', index, name='card'),
]
