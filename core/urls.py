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
    path('<int:id>/alterar_receita', views.alterar_receita, name= 'alterar_receita'),
    path('<int:id>/cadastrar_despesa', views.cadastrar_despesa, name= 'cadastrar_despesa'),
    path('<int:id>/alterar_despesa', views.alterar_despesa, name= 'alterar_despesa'),
    path('buscar', views.buscar, name= 'buscar'),
    path('despesa/<int:id>/apagar', views.apagar_despesa, name='apagar_despesa'),
    path('receita/<int:id>/apagar', views.apagar_receita, name='apagar_receita'),
]