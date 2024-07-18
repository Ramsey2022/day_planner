from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("weather/", views.weather, name="weather"),
    path("parks/", views.parks, name="parks"),
    path("home/", views.home, name="home"),
]
