from django.urls import path

from PluginBackend.views.download import *
from PluginBackend.views.plugin import *


urlpatterns = [
    path('file/<int:id>/', DownloadView.as_view(), name='file'),
    path('plugin/<CharField:dict_key>/', PluginView.as_view(), name='plugin'),
    
]
