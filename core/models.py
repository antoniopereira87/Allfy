from django.db import models


class cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=150)
