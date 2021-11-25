from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from Web.models import *


def index(request):
    return render(request, "web/index.html", {"user": request.user})