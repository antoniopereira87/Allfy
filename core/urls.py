from django.urls import path

from .views import index
from . import views

urlpatterns = [
    path('', index),
    path('cadastrar', views.cadastrar, name= 'cadastrar'),
    path('login', views.login, name= 'login'),
] 