from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=72)
#    description = models.TextField(default='')
#    birthday = models.TextField(default='')
#    username = models.CharField(max_length=20, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"