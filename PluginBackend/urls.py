from django.urls import path

from PluginBackend.views.download import *


urlpatterns = [
    path('file/<int:id>/', DownloadView.as_view(), name='file'),
    
]
