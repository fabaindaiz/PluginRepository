from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Logs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.action

class ApiKey(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name