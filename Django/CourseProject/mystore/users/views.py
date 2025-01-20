from django.contrib.auth import login, logout
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ви успішно зареєструвались!")
            return redirect("catalog")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "users/login.html"


def logout_view(request):
    logout(request)
    messages.info(request, "Ви вийшли з системи.")
    return redirect("catalog")


@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})
