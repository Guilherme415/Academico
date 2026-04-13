from django.contrib import admin
from .models import *

# ========================
# INLINES
# ========================

# i) Ocupação -> Pessoas
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

# ii) Instituição -> Cursos
class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

# iii) Área do Saber -> Cursos
class CursoInlineArea(admin.TabularInline):
    model = Curso
    extra = 1

# iv) Cursos -> Disciplinas
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

# v) Disciplinas -> Avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

# ix) Pessoa -> tudo relacionado
class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1


# ========================
# ADMINS
# ========================

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInlineArea]

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]


admin.site.register(Cidade)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(AvaliacaoTipo)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Avaliacao)
admin.site.register(Turma) 
admin.site.register(Matricula)
admin.site.register(Frequencia)
admin.site.register(Turnos)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)