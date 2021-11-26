from django.urls import path, include
from . import views


urlpatterns = [
    path('file', views.download_file, name='file'),
    
]
