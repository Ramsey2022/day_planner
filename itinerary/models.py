from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    postal_code = models.CharField(
        max_length=6,
    )
