# transcription/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('transcribe/', views.transcribe, name='transcribe'),
]
