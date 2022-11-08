from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('catalog.urls', namespace='catalog')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('about/', include('cookbook.urls', namespace='cookbook')),
    path('contact/', include('customer.urls', namespace='customer')),
    path('', include('homepage.urls', namespace='hone')),
    path('order/', include('order.urls', namespace='order')),
    path('accounts/', include('userapp.urls', namespace='userapp')),
    path('api/v1/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
