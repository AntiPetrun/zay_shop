from django.urls import path
from .views import ProductListView, MenProductListView, \
    WomenProductListView, UnisexProductListView, CategoryProductListView,\
    ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='shop'),
    path('men/', MenProductListView.as_view(), name='shop_men'),
    path('women/', WomenProductListView.as_view(), name='shop_women'),
    path('unisex/', UnisexProductListView.as_view(), name='shop_unisex'),
    path('category_products/<slug:cat_slug>/', CategoryProductListView.as_view(), name='cat_prods'),
    path('<slug:prod_slug>/<int:brand>/<int:gender>/', ProductDetailView.as_view(), name='prod_card'),
]
