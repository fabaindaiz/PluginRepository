from django import forms
from django.forms.widgets import HiddenInput

from PluginBackend.models import *


class ServerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    port = forms.CharField(label='Port', max_length=10)
    server_id = forms.CharField(label='Server ID', max_length=100)

    def __init__(self, *args, **kwargs):
        super(ServerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PluginForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    code = forms.CharField(label='Code', max_length=10)
    folder_name = forms.CharField(label='Folder Name', max_length=100)

    def __init__(self, *args, **kwargs):
        super(PluginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ServerDetailsForm(forms.Form):
    server = forms.CharField(widget=forms.HiddenInput(), label='Server', max_length=100)
    plugin = forms.ModelChoiceField(queryset=Plugin.objects.all())

    def __init__(self, *args, **kwargs):
        super(ServerDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PluginDetailsForm(forms.Form):
    plugin = forms.CharField(widget=forms.HiddenInput(), label='Plugin', max_length=100)
    version = forms.CharField(label='Version', max_length=50)
    file = forms.FileField(label='File')

    def __init__(self, *args, **kwargs):
        super(PluginDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)