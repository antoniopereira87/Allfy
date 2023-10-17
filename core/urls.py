from django.urls import path

from .views import index
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('cadastrar', views.cadastrar, name= 'cadastrar'),
    path('login', views.access_login, name= 'login'),
    path('user_area/<int:id>', views.user_area, name= 'user_area'),
    path('logout', views.logout_view, name= 'logout'),
    path('<int:id>/cadastrar_receita', views.cadastrar_receita, name= 'cadastrar_receita'),
]