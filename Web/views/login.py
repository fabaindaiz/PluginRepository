from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View

from PluginRepository.util import *
from Web.models import *
from Web.forms import *


def login_required(function):
    def wrapper(request, *args, **kw):
        if request.user.is_authenticated:
            logout(request)
        return function(request, *args, **kw)
    return wrapper

class LoginView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request):
        login_form = LoginForm()
        return render(request,"web/login.html", {"user": request.user, "form": login_form})
    
    def post(self, request):
        if "LoginForm" in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    Logs(user=user, action="User Login", description="From "+get_client_ip(request)).save()
                    return redirect('/')
        return redirect('/login')
