from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

from PluginBackend.models import *


def download_file(request, id = None):
    if not request.user.is_authenticated:
        return redirect('/login')

    elif request.method == "GET" and id:
        plugin = get_object_or_404(PluginVersion, id=id)
        response = HttpResponse(plugin.file, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + plugin.file_name
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