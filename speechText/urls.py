from django.conf.urls import url 
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send-audio/', views.audio_data, name='audio-data')
]       