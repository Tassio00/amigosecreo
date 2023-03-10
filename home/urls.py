from django.urls import path
from . import views

urlpatterns = [
    path ('' , views.home, name= "home"),
    path ('dellUsuario/<int:id>', views.dellUsuario, name= "dellUsuario"),
    path ('editUsuario/<int:id>', views.editUsuario, name= "editUsuario"),
    
]