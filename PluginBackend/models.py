from django.db import models
from django.utils import timezone
from Web.models import User


class Server(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Plugin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    code = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

class PluginVersion(models.Model):
    id = models.AutoField(primary_key=True)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    version = models.CharField(max_length=200)
    file = models.FileField(upload_to='plugins/')
    file_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_name

class PluginServer(models.Model):
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    version = models.ForeignKey(PluginVersion, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_name

