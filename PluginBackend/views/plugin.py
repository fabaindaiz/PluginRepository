from django.shortcuts import redirect, get_object_or_404, get_list_or_404
from django.utils.crypto import get_random_string
from django.http import HttpResponse, JsonResponse
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *
from Web.models import *


class PluginView(View):

    def get(self, request, dict_key):
        plugin = get_object_or_404(PluginDictionary, key=dict_key).plugin
        response = HttpResponse(plugin.file, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + plugin.file_name
        Logs(user=request.user, action='File Downloaded', description=plugin.file_name).save()
        return response
    
    def post(self, request, dict_key):
        post_server = request.POST['server']
        post_key = request.POST['key']
        model_key = get_object_or_404(ApiKey, name = "plugin")
        if model_key.key != post_key:
            return JsonResponse(data={"response": "error"}, safe=False)

        for instance in get_list_or_404(PluginDictionary, server=post_server):
            instance.delete()

        server = get_list_or_404(ServerPlugin, server = post_server)
        for plugin in server:
            last = get_list_or_404(PluginVersion, plugin = plugin.name).order_by('-update_date')[0]
            plugin.version = last.version
            plugin.file_name = last.file_name
            plugin.save()
            instance = PluginDictionary(key=get_random_string(length=32), server=plugin.server, plugin=last)
            instance.save()
            
        dict = get_list_or_404(PluginDictionary, server = post_server)
        return JsonResponse(data={"response": "success", "dict": dict}, safe=False)
        