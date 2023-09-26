from django.db import models


class cliente(models.Model):
    first_name = models.CharField('Nome', max_length=150)
    last_name = models.CharField('Nome', max_length=150)
    email = models.EmailField('E-mail')
