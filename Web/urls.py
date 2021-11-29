from Web.views_.plugin import *
from Web.views_.server import *
from Web.views_.login import *
from django.urls import path
from . import views


urlpatterns = [
    # Views methods
    path('', views.Index, name='index'),

    path('settings/', views.SettingsPage, name='plugin'),
    path('logs/', views.LogsPage, name='plugin'),

    path('error/', views.Error, name='error'),
    path('error/<int:error>/', views.Error, name='error'),

    # Views class-based
    path('login/', LoginView.as_view(), name='login'),

    path('server/', ServerView.as_view(), name='server'),
    path('server/<int:id>/', ServerView.as_view(), name='server'),

    path('plugin/', PluginView.as_view(), name='plugin'),
    path('plugin/<int:id>/', PluginView.as_view(), name='plugin'),
    
]
