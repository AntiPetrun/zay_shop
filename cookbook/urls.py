from django.urls import path
from .views import BrandListView

app_name = 'cookbook'

urlpatterns = [
    path('', BrandListView.as_view(), name='about'),
]
