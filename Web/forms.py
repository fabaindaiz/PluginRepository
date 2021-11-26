from django import forms
from django.forms.widgets import HiddenInput

from PluginBackend.models import *


class ServerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    port = forms.CharField(label='Port', max_length=10)
    server_id = forms.CharField(label='Server ID', max_length=100)

class PluginForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    code = forms.CharField(label='Code', max_length=10)
    folder_name = forms.CharField(label='Folder Name', max_length=100)

class PluginVersionForm(forms.Form):
    plugin = forms.ModelChoiceField(queryset=Plugin.objects.all())
    version = forms.CharField(label='Version', max_length=50)
    file = forms.FileField(label='File')

class ServerPluginForm(forms.Form):
    server = forms.ModelChoiceField(queryset=Server.objects.all())
    plugin = forms.ModelChoiceField(queryset=Plugin.objects.all())

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)