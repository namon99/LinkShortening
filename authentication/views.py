from django.views.generic import TemplateView, CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm


class LoginView(auth_views.LoginView):
    template_name = 'authentication/login.html'


class LogoutView(auth_views.LogoutView):
    pass


class SignUpView(CreateView):
    template_name = 'authentication/signup.html'
    form_class = UserCreationForm


class ProfileView(TemplateView):
    template_name = 'authentication/profile.html'
