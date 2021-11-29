from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *
from Web.models import *
from Web.forms import *

class SettingsView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, error = 404):
        return render(request, "web/settings.html", {})