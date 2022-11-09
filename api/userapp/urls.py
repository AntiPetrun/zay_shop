from django.urls import path, include
from .views import ProductViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
