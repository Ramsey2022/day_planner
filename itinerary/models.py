from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    postal_code = models.CharField(
        max_length=6,
    )

    class Meta:
        db_table = "profile"
