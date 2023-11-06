from django.contrib import admin
from api_consultas_medicas.models import PessoaProfissional, Consulta

class PessoasProfissionais(admin.ModelAdmin):
    list_display = ('id','nome','especialidade')
    list_display_links = ('id','nome',)
    search_fields = ("nome",)

admin.site.register(PessoaProfissional, PessoasProfissionais)

class Consultas(admin.ModelAdmin):
    list_display = ('data_consulta','pessoa_profissional')
    list_display_links = ('data_consulta','pessoa_profissional')
    #search_fields = ("nome",)

admin.site.register(Consulta, Consultas)

