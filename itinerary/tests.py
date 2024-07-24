from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class WeatherViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test1!",
        )
        self.client = Client()

    def test_weather(self):
        self.client.login(username="test", password="test1!")
        url = reverse("weather")
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)


class ParksViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test1!",
        )
        self.client = Client()

    def test_parks(self):
        self.client.login(username="test", password="test1!")
        url = reverse("parks")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class HomeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test1!",
        )
        self.client = Client()

    def test_home(self):
        self.client.login(username="test", password="test1!")
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class IndexViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test1!",
        )
        self.client = Client()

    def test_index(self):
        self.client.login(username="test", password="test1!")
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class SignupViewTest(TestCase):
    def test_signup(self):
        url = reverse("signup")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test1!",
        )
        self.client = Client()

    def test_login(self):
        self.client.login(username="test", password="test1!")
        url = reverse("login")
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 200)


class LogoutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test1!",
        )
        self.client = Client()

    def test_logout(self):
        self.client.login(username="test", password="test1!")
        url = reverse("logout")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
