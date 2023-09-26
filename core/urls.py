from django.urls import path

from .views import index, cadastrar
from . import views

urlpatterns = [
    path('', index),
    path('cadastrar', cadastrar),
    # path('cadastrar', views.SignUp.as_view(), name= 'cadastrar'),
] 