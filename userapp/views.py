from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, SignInForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'userapp/signup.html'
    success_url = reverse_lazy('userapp:login')


class LogInView(LoginView):
    template_name = 'userapp/login.html'
    form_class = SignInForm
