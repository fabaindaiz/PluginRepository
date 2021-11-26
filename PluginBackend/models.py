from django.db import models
from django.utils import timezone
from Web.models import User


class Server(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    port = models.CharField(max_length=10, default="25565")
    server_id = models.CharField(max_length=100, default="")
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Plugin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, default='-1')
    folder_name = models.CharField(max_length=100)
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class PluginVersion(models.Model):
    id = models.AutoField(primary_key=True)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    file = models.FileField(upload_to='PluginBackend/plugins/')
    file_name = models.CharField(max_length=200)
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_name

class ServerPlugin(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    plugin = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    version = models.ForeignKey(PluginVersion, blank=True, null=True, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200, default="null")
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file_name
