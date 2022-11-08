from django.urls import path
from .views import SignUpView, LogInView, ProfileView
from django.contrib.auth.views import LogoutView

app_name = 'userapp'

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login', LogInView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
]
