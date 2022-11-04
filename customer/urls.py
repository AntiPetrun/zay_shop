from django.urls import path
from .views import ContactTemplateView

app_name = 'customer'

urlpatterns = [
    path('', ContactTemplateView.as_view(), name='contact'),
]
