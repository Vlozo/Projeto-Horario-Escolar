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

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Club, ClubAdmin)

# Register your models here.
