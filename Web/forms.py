from django import forms
from django.forms.widgets import HiddenInput

from PluginBackend.models import *


class AbstractForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AbstractForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class ServerForm(AbstractForm):
    name = forms.CharField(label='Name', max_length=100)
    port = forms.CharField(label='Port', max_length=10)
    server_id = forms.CharField(label='Server ID', max_length=100)

class PluginForm(AbstractForm):
    name = forms.CharField(label='Name', max_length=100)
    code = forms.CharField(label='Code', max_length=10)
    folder_name = forms.CharField(label='Folder Name', max_length=100)

class ServerDetailsForm(AbstractForm):
    server = forms.CharField(widget=forms.HiddenInput(), label='Server', max_length=100)
    plugin = forms.ModelChoiceField(queryset=Plugin.objects.all())

class PluginDetailsForm(AbstractForm):
    plugin = forms.CharField(widget=forms.HiddenInput(), label='Plugin', max_length=100)
    version = forms.CharField(label='Version', max_length=50)
    file = forms.FileField(label='File')

class LoginForm(AbstractForm):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
