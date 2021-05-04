from django.urls import path, include
from . import views

app_name = 'sistema'

url_patterns = [
    path('cadastro_aluno', views.cadastro_aluno, name='cadastro_aluno'),
    path('cadastro_instrutor', views.cadastro_instrutor, name='cadastro_instrutor'),
    path('cadastro_treino', views.cadastro_treino, name='cadastro_treino'),
    path('cadastro_turma', views.cadastro_turma, name='cadastro_turma')
]