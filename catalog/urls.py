from django.urls import path
from .views import ProductListView, CategoryProductListView, ProductDetailView, \
    GenderProductListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='shop'),
    path('<int:gender>/', GenderProductListView.as_view(), name='gender_prods'),
    path('<slug:cat_slug>/', CategoryProductListView.as_view(), name='cat_prods'),
    path('<slug:prod_slug>/<int:brand>/<int:gender>/', ProductDetailView.as_view(), name='prod_card'),
]
