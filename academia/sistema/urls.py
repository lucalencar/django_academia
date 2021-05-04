from django.urls import path, include
from . import views

app_name = 'sistema'

urlpatterns = [
    path('cadastro_aluno', views.cadastro_aluno, name='cadastro_aluno'),
    path('cadastro_instrutor', views.cadastro_instrutor, name='cadastro_instrutor'),
    path('cadastro_treino', views.cadastro_treino, name='cadastro_treino'),
    path('cadastro_turma', views.cadastro_turma, name='cadastro_turma'),
    path('inicio', views.inicio, name='inicio'),
    path('form_cadastro_aluno', views.form_cadastro_aluno, name='form_cadastro_aluno'),
    path('form_cadastro_instrutor', views.form_cadastro_instrutor, name='form_cadastro_instrutor'),
    path('form_cadastro_treino', views.form_cadastro_treino, name='form_cadastro_treino'),
    path('form_cadastro_turma', views.form_cadastro_turma, name='form_cadastro_turma'),
    path('visualizar_aluno/<int:user_id>', views.visualizar_aluno, name='visualizar_aluno'),
    path('visualizar_instrutor/<int:user_id>', views.visualizar_instrutor, name='visualizar_instrutor')
]