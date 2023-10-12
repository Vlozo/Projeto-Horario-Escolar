from django.contrib import admin
from .models import *

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("turma",)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "turma",)
    list_filter = ("turma",)
    search_fields = ("nome",)

class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ("nome", "telefone", "dependente",)
    search_fields = ("nome",)

class ClubAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('matricula', 'data_nascimento', 'email', 'telefone', 'senha')

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Usuario, UsuarioAdmin)

# Register your models here.
