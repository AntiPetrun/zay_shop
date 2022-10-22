from django.urls import path
from .views import index

app_name = 'comment'

urlpatterns = [
    path('', index, name='comments'),
]
