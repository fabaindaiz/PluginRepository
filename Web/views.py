from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from PluginBackend.models import *
from Web.models import *
from Web.forms import *


def Index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "web/index.html", {})

def ServerPage(request, id = None):
    if not request.user.is_authenticated:
        return redirect('login')

    elif request.method == "GET":
        if  not id:
            data = Server.objects.all()
            form = ServerForm()
            return render(request, "web/server.html", {"data": data, "form": form})
        else:
            server = Server.objects.get(id=id)
            data = ServerPlugin.objects.filter(server=server).order_by('-update_date')
            form = ServerDetailsForm()
            form.fields['server'].initial = server
            return render(request, "web/serverdetails.html", {"user": request.user, "server": server, "data": data, "form": form})
    
    elif request.method == "POST":
        if "ServerForm" in request.POST:
            form = ServerForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                port = form.cleaned_data['port']
                server_id = form.cleaned_data['server_id']
                instance = Server(name=name, port=port, server_id=server_id)
                instance.save()
        elif "ServerDetailsForm" in request.POST:
            form = ServerDetailsForm(request.POST)
            if form.is_valid():
                server = Server.objects.get(name=form.cleaned_data['server'])
                plugin = Plugin.objects.get(name=form.cleaned_data['plugin'])
                instance = ServerPlugin(server=server, plugin=plugin)
                instance.save()
    return redirect('server')

def PluginPage(request, id = None):
    if not request.user.is_authenticated:
        return redirect('login')

    elif request.method == "GET":
        if not id:
            data = Plugin.objects.all()
            form = PluginForm()
            return render(request, "web/plugin.html", {"data": data, "form": form})
        else:
            plugin = Plugin.objects.get(id=id)
            data = PluginVersion.objects.filter(plugin=plugin).order_by('-update_date')
            form = PluginDetailsForm()
            form.fields['plugin'].initial = plugin
            return render(request, "web/plugindetails.html", {"user": request.user, "plugin": plugin, "data": data, "form": form})
    
    elif request.method == "POST":
        if "PluginForm" in request.POST:
            form = PluginForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                code = form.cleaned_data['code']
                name = form.cleaned_data['folder_name']
                instance = Plugin(name=name, code=code, folder_name=name)
                instance.save()
        elif "PluginDetailsForm" in request.POST:
            form = PluginDetailsForm(request.POST, request.FILES)
            if form.is_valid():
                plugin = Plugin.objects.get(name=form.cleaned_data['plugin'])
                version = form.cleaned_data['version']
                file = form.files['file']
                name = plugin.folder_name + "-" + version + ".jar"
                instance = PluginVersion(plugin=plugin, version=version, file=file, file_name=name)
                instance.save()
    return redirect(request.path_info)

def LoginPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

    elif request.method == 'GET':
        login_form = LoginForm()
        return render(request,"web/login.html", {"user": request.user, "form": login_form})

    elif request.method == 'POST':
        if "LoginForm" in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        return redirect('login')

def SettingsPage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "web/settings.html", {})

def LogsPage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, "web/logs.html", {})