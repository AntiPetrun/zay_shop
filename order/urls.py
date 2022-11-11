from django.urls import path
from .views import AddToBasket, DeleteFromBasket

app_name = 'order'

urlpatterns = [
    path('', AddToBasket.as_view(), name='add_to_basket'),
    path('<int:pk>/delete/', DeleteFromBasket.as_view(), name='del_from_basket'),
]
