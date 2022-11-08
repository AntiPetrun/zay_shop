from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, SignInForm
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'userapp/signup.html'
    success_url = reverse_lazy('userapp:login')


class LogInView(LoginView):
    template_name = 'userapp/login.html'
    form_class = SignInForm


class ProfileView(LoginRequiredMixin, View):
    template_name = 'userapp/profile.html'
    login_url = reverse_lazy('userapp:login')

    def get(self, request):
        user = self.request.user
        return render(request, self.template_name, {'user': user})
