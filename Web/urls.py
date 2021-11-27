from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('server', views.ServerPage, name='server'),
    path('plugin', views.PluginPage, name='plugin'),

    path("login", views.LoginPage, name="login"),
    
]
