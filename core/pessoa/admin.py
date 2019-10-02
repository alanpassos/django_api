from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    display_list = ['nome','ativo']


admin.site.register(Pessoa, PessoaAdmin)