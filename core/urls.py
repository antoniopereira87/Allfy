from django.urls import path

from .views import index
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('cadastrar', views.cadastrar, name= 'cadastrar'),
    path('login', views.access_login, name= 'login'),
    path('user_area', views.user_area, name= 'user_area'),
]