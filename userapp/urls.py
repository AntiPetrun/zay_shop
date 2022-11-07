from django.urls import path
from .views import SignUpView, LogInView
from django.contrib.auth.views import LogoutView

app_name = 'userapp'

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LogInView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('profile', HomeTemplateView.as_view(), name='profile'),
]
