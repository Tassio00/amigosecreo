from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField("nome", max_length=50)
    email = models.EmailField("email", max_length=254)


    
