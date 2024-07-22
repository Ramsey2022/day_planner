from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
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
        postal_code = request.POST.get("postal_code")
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
                    username=username,
                    password=make_password(password),
                    postal_code=postal_code,
                )
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
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
                return HttpResponseRedirect(reverse("home"))
        except User.DoesNotExist:
            return render(request, "login.html", {"form": LoginForm})
    return render(request, "login.html", {"form": LoginForm})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "index.html")


def home(request):
    if request.user.is_authenticated:
        zipcode = {"postal_code": request.user.profile.postal_code}
        weather = req.get("http://weather_api:8080/forecast", json=zipcode)
        parks = req.post("http://parks_api:8060/parks", json=zipcode)
        weather_data = weather.json()
        park_data = parks.json()

        weather_item = weather_data[0:1]
        park_item = park_data[0:5]
        return render(
            request,
            "loggedin_index.html",
            {"weather_data": weather_item, "park_data": park_item},
        )
    else:
        return HttpResponseRedirect(reverse("login"))


def weather(request):
    if request.user.is_authenticated:
        zipcode = {"postal_code": request.user.profile.postal_code}
        weather = req.get("http://weather_api:8080/forecast", json=zipcode)
        data = weather.json()
        return render(request, "weather.html", {"weather_data": data})
    else:
        return HttpResponseRedirect(reverse("login"))


def parks(request):
    if request.user.is_authenticated:
        zipcode = {"postal_code": request.user.profile.postal_code}
        parks = req.post("http://parks_api:8060/parks", json=zipcode)
        data = parks.json()
        return render(request, "parks.html", {"park_data": data})
    else:
        return HttpResponseRedirect(reverse("login"))
