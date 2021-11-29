from django.urls import path

from Web.views.settings import *
from Web.views.plugin import *
from Web.views.server import *
from Web.views.index import *
from Web.views.login import *
from Web.views.error import *
from Web.views.logs import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),    

    path('server/', ServerView.as_view(), name='server'),
    path('server/<int:id>/', ServerView.as_view(), name='server'),

    path('plugin/', PluginView.as_view(), name='plugin'),
    path('plugin/<int:id>/', PluginView.as_view(), name='plugin'),

    path('settings/', SettingsView.as_view(), name='plugin'),
    path('logs/', LogsView.as_view(), name='plugin'),

    path('error/', ErrorView.as_view(), name='error'),
    path('error/<int:error>/', ErrorView.as_view(), name='error'),
    
]
