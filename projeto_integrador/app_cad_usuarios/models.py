from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    endereco = models.TextField(max_length= 200)
    cep = models.CharField(max_length=9)
    condominio = models.TextField(max_length=20)
