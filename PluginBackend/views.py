from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from PluginBackend.models import *


def download_file(request):
    if not request.user.is_authenticated:
        return redirect('login')

    elif request.method == "GET":
        id = request.GET.get('id')
        if id:
            plugin = Plugin.objects.get(id=request.GET.get('id'))
            version = PluginVersion.objects.filter(plugin=plugin).order_by('-update_date')[0]
            response = HttpResponse(version.file, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + version.file_name
            return response
    return redirect('/')

def delete(request):
    if not request.user.is_authenticated or not request.is_ajax():
        return JsonResponse(data={}, safe=False)

    elif request.method == "GET":
        model = request.GET.get('m')
        id = request.GET.get('id')
        if not model or not id:
            pass
        elif model == "Server":
            Server.objects.get(id=id).delete()
        elif model == "Plugin":
            Plugin.objects.get(id=id).delete()
        elif model == "PluginVersion":
            PluginVersion.objects.get(id=id).delete()
        elif model == "PluginServer":
            ServerPlugin.objects.get(id=id).delete()
    return JsonResponse(data={}, safe=False)