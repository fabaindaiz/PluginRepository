from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('login', views.LoginPage, name='login'),

    path('server', views.ServerPage, name='server'),
    path('server/<int:id>', views.ServerPage, name='server'),

    path('plugin', views.PluginPage, name='plugin'),
    path('plugin/<int:id>', views.PluginPage, name='plugin'),

    path('settings', views.SettingsPage, name='plugin'),
    path('logs', views.LogsPage, name='plugin'),
    
]
