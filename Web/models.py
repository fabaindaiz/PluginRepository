from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from PluginBackend.models import Plugin


class User(AbstractUser):
    pass

class Logs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.action

class ApiKey(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PluginDictionary(models.Model):
    key = models.CharField(max_length=50)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name