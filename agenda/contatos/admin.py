from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'sobrenome', 'categoria', 'telefone', 'email', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('categoria')
    list_per_page = 15
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

