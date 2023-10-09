from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import RegistrationForm
from .apps import AppConfig


# Create your views here.
def home(request: HttpRequest):
    return render(request, f"{AppConfig.name}/home.html")


def register(request: HttpRequest):
    # return render(request, "register.html")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            return render(request, "success.html")
            # return redirect("/")
    else:
        form = RegistrationForm()
        return render(request, "register.html", {"form": form})


def about(request: HttpRequest):
    return render(request, "about.html")
