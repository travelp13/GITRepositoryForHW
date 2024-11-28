from django.contrib.auth.views import LoginView
from .forms import StandardLoginForm, CustomLoginForm


class StandardLoginView(LoginView):
    template_name = "accounts/standard_login.html"
    form_class = StandardLoginForm


class CustomLoginView(LoginView):
    template_name = "accounts/custom_login.html"
    form_class = CustomLoginForm
