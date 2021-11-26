from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_user, name="login"),

    path('server', views.ServerPage, name='server'),
    path('plugin', views.PluginPage, name='plugin'),
    
]
