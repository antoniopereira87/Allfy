from django.urls import path

from .views import index, cadastrar

urlpatterns = [
    path('', index),
    path('cadastrar', cadastrar),
] 