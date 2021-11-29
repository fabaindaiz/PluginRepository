from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from PluginRepository.util import *


class ErrorView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, error = 404):
        message = {400: "Bad Request", 401: "Unauthorized", 403: "Forbidden", 404: "Not Found", 500: "Internal Server Error", 501: "Not Implemented", 502: "Bad Gateway", 503: "Service Unavailable", 504: "Gateway Timeout"}
        return render(request, "web/error.html", {"error": error, "message": message.get(error, "Unknown error")})