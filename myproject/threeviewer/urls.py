from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_viewer, name='model_viewer'),
]
