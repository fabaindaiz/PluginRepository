from os import name, urandom
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from PluginBackend.models import *
from Web.models import *
from Web.forms import *


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    elif request.method == "GET":
        server_data = Server.objects.all()
        plugin_data = Plugin.objects.all()
        server_form = ServerForm()
        plugin_form = PluginForm()
        form = {"server": server_form, "plugin": plugin_form}
        return render(request, "web/index.html", {"form": form, "server_data": server_data, "plugin_data": plugin_data})
    
    elif request.method == "POST":
        if "ServerForm" in request.POST:
            form = ServerForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                port = form.cleaned_data['port']
                server_id = form.cleaned_data['server_id']
                instance = Server(name=name, port=port, server_id=server_id)
                instance.save()
        if "PluginForm" in request.POST:
            form = PluginForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                code = form.cleaned_data['code']
                folder_name = form.cleaned_data['folder_name']
                instance = Plugin(name=name, code=code, folder_name=folder_name)
                instance.save()
    return redirect('/')

def ServerPage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    elif request.method == "GET":
        id = request.GET.get('id')
        if id:
            server = Server.objects.get(id=id)
            server_table = ServerPlugin.objects.filter(server=server).order_by('-update_date')
        else:
            server = None
            server_table = ServerPlugin.objects.all()
        server_form = ServerPluginForm()
        return render(request, "web/server.html", {"server": server, "data": server_table, "form": server_form})
    
    elif request.method == "POST":
        if "ServerForm" in request.POST:
            form = ServerPluginForm(request.POST)
            if form.is_valid():
                server = Server.objects.get(name=form.cleaned_data['server'])
                plugin = Plugin.objects.get(name=form.cleaned_data['plugin'])

                instance = ServerPlugin(server=server, plugin=plugin)
                instance.save()
    return redirect('server')

def PluginPage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    elif request.method == "GET":
        id = request.GET.get('id')
        if id:
            plugin = Plugin.objects.get(id=id)
            plugin_table = PluginVersion.objects.filter(plugin=plugin).order_by('-update_date')
        else:
            plugin = None
            plugin_table = PluginVersion.objects.all().order_by('-update_date')
        plugin_form = PluginVersionForm()
        return render(request, "web/plugin.html", {"plugin": plugin, "data": plugin_table, "form": plugin_form})
    
    elif request.method == "POST":
        if "PluginForm" in request.POST:
            form = PluginVersionForm(request.POST, request.FILES)
            if form.is_valid():
                plugin = Plugin.objects.get(name=form.cleaned_data['plugin'])
                version = form.cleaned_data['version']
                file = form.files['file']
                file_name = plugin.name + "-" + version + ".jar"

                instance = PluginVersion(plugin=plugin, version=version, file=file, file_name=file_name)
                instance.save()
    return redirect('plugin')

# Muestra la pagina de login
def login_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')

    elif request.method == 'GET':
        login_form = LoginForm()
        return render(request,"web/login.html", {"form": login_form})

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
                else:
                    messages.error(request, "Usuario o contraseña incorrectos")
                    return redirect('login')
        return redirect('login')
