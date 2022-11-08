from django.urls import path, include

urlpatterns = [
    path('shop/', include('api.catalog.urls')),
]
