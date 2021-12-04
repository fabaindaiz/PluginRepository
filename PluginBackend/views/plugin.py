from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *
from Web.models import *


class DownloadView(View):

    def get(self, request, plugin_id):
        pass
    
    def post(self, request):
        post_key = request.POST['key']
        model_key = get_object_or_404(ApiKey, name = "plugin")
        if model_key.key != post_key:
            return HttpResponse("null")



        server_id = request.POST['id']
        plugin_id = request.POST['plugin_id']
        

        plugin = get_object_or_404(PluginVersion, id=id)
        response = HttpResponse(plugin.file, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + plugin.file_name
        Logs(user=request.user, action='File Downloaded', description=plugin.file_name).save()
        return response
        