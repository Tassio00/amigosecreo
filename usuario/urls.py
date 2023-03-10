
from django.urls import path
from . import views


urlpatterns = [
    path('', views.usuario, name = "usuario"),
    path('aicionaUsuario/', views.addUsuario, name="addUsuario")
]
