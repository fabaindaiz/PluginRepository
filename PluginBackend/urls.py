from django.urls import path, include
from . import views


urlpatterns = [
    path('file/<int:id>/', views.download_file, name='file'),
    
]
