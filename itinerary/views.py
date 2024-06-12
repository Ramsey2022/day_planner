from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import make_password
import requests as req

from itinerary.forms import LoginForm, SignUpForm


# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.filter(username=username).first()
            if user:
                return render(
                    request,
                    "signup.html",
                    {"form": SignUpForm, "message": "user already exists"},
                )
            else:
                user = User.objects.create(
                    username=username, password=make_password(password)
                )
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return render(request, "signup.html", {"form": SignUpForm})
    return render(request, "signup.html", {"form": SignUpForm})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return render(request, "login.html", {"form": LoginForm})
    return render(request, "login.html", {"form": LoginForm})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def index(request):
    return render(request, "index.html")


def weather(request):
    weather = req.get("http://weather-api:8080/forecast")
    weather_data = HttpResponse(weather, content_type="application/json")
    print(weather_data)
    return render(request, "weather.html", {"weather_data": weather_data})


def parks(request):
    parks = req.get("http://parks-api:8060/parks")
    parks_data = HttpResponse(parks).json()
    print(parks_data.text)
    return render(request, "parks.html", {"parks": parks_data["park_data"]})
