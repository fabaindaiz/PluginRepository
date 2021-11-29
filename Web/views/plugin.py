from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *
from Web.models import *
from Web.forms import *


class PluginView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, id = None):
        if not id:
            data = Plugin.objects.all()
            form = PluginForm()
            return render(request, "web/plugin.html", {"data": data, "form": form})
        else:
            plugin = get_object_or_404(Plugin, id=id)
            data = PluginVersion.objects.filter(plugin=plugin).order_by('-update_date')
            form = PluginDetailsForm()
            form.fields['plugin'].initial = plugin
            return render(request, "web/plugindetails.html", {"user": request.user, "plugin": plugin, "data": data, "form": form})
    
    def post(self, request, id = None):
        if "PluginForm" in request.POST:
            form = PluginForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                code = form.cleaned_data['code']
                name = form.cleaned_data['folder_name']
                instance = Plugin(name=name, code=code, folder_name=name)
                instance.save()
                Logs(user=request.user, action="Plugin Created", description=name).save()
        elif "PluginDetailsForm" in request.POST:
            form = PluginDetailsForm(request.POST, request.FILES)
            if form.is_valid():
                plugin = get_object_or_404(Plugin, name=form.cleaned_data['plugin'])
                version = form.cleaned_data['version']
                file = form.files['file']
                name = plugin.folder_name + "-" + version + ".jar"
                instance = PluginVersion(plugin=plugin, version=version, file=file, file_name=name)
                instance.save()
                Logs(user=request.user, action="Plugin Uploaded", description=name).save()
        return redirect(request.path_info)