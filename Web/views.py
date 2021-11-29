from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

from Web.models import *
from Web.forms import *


@require_http_methods(["GET"])
def Index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "web/index.html", {}) 

@require_http_methods(["GET", "POST"])
def SettingsPage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "web/settings.html", {})

@require_http_methods(["GET"])
def LogsPage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "web/logs.html", {})

@require_http_methods(["GET"])
def Error(request, error = 404):
    if not request.user.is_authenticated:
        return redirect('login')

    message = {400: "Bad Request", 401: "Unauthorized", 403: "Forbidden", 404: "Not Found", 500: "Internal Server Error", 501: "Not Implemented", 502: "Bad Gateway", 503: "Service Unavailable", 504: "Gateway Timeout"}
    return render(request, "web/error.html", {"error": error, "message": message.get(error, "Unknown error")})