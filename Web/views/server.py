from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *
from Web.models import *
from Web.forms import *


class ServerView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, id = None):
        if  not id:
            data = Server.objects.all()
            form = ServerForm()
            return render(request, "web/server.html", {"data": data, "form": form})
        else:
            server = get_object_or_404(Server, id=id)
            data = ServerPlugin.objects.filter(server=server).order_by('-update_date')
            form = ServerDetailsForm()
            form.fields['server'].initial = server
            return render(request, "web/serverdetails.html", {"user": request.user, "server": server, "data": data, "form": form})
    
    def post(self, request, id = None):
        if "ServerForm" in request.POST:
            form = ServerForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                port = form.cleaned_data['port']
                server_id = form.cleaned_data['server_id']
                instance = Server(name=name, port=port, server_id=server_id)
                instance.save()
                Logs(user=request.user, action="Server Created", description=name).save()
        elif "ServerDetailsForm" in request.POST:
            form = ServerDetailsForm(request.POST)
            if form.is_valid():
                server = get_object_or_404(Server, name=form.cleaned_data['server'])
                plugin = get_object_or_404(Plugin, name=form.cleaned_data['plugin'])
                instance = ServerPlugin(server=server, plugin=plugin)
                instance.save()
                Logs(user=request.user, action="Server Modified", description=server.name+" - "+plugin.name).save()
        return redirect(request.path_info)