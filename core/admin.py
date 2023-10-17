from django.contrib import admin
from .models import Income, Profile


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        'valor',
        'descricao',
    )
    search_fields = ('valor', 'descricao')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )
    search_fields = ('user',)