from django.urls import path
from .views import index

app_name = 'customer'

urlpatterns = [
    path('', index, name='customer'),
]
