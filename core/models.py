from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.choices import CATEGORIA

# Aplicar o uso do método construtor nas classes 

class Profile(models.Model):
    foto = models.ImageField(null=True)
    nome = models.CharField(null=True, blank=True, max_length=150)
    user = models.OneToOneField('auth.user', related_name= 'profile', verbose_name= 'Usuário', on_delete= models.CASCADE )
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return str(self.pk)


class Income(models.Model):
    valor = models.FloatField()  
    descricao = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, related_name= 'income', on_delete= models.CASCADE )
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        
    def __str__(self):
        return str(self.pk)
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Expense(models.Model):
    valor = models.FloatField()
    categoria = models.CharField(choices = CATEGORIA, max_length=30)  
    descricao = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, related_name= 'expense', on_delete= models.CASCADE )
    class Meta:
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"
        
    def __str__(self):
        return str(self.pk)
