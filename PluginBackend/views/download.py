from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views import View

from PluginRepository.util import *
from PluginBackend.models import *
from Web.models import *


class DownloadView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, id):
        plugin = get_object_or_404(PluginVersion, id=id)
        response = HttpResponse(plugin.file, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + plugin.file_name
        Logs(user=request.user, action='File Downloaded', description=plugin.file_name).save()
        return response