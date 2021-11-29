from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *


class DeleteView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
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