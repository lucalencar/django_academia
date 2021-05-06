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
    path('visualizar_instrutor/<int:user_id>', views.visualizar_instrutor, name='visualizar_instrutor'),
    path('visualizar_treino/<int:user_id>', views.visualizar_treino, name='visualizar_treino'),
    path('visualizar_turma/<int:user_id>', views.visualizar_turma, name='visualizar_turma'),
    path('atualizar_alunos', views.atualizar_alunos, name='atualizar_alunos'),
    path('atualizar_dados_aluno/<int:user_id>', views.atualizar_dados_aluno, name='atualizar_dados_aluno'),
    path('atualizar_instrutor', views.atualizar_instrutor, name='atualizar_instrutor'),
    path('atualizar_treino', views.atualizar_treino, name='atualizar_treino'),
    path('atualizar_turma', views.atualizar_turma, name='atualizar_turma'),
    path('atualizar_dados_turma/<int:user_id>', views.atualizar_dados_turma, name='atualizar_dados_turma'),
    path('atualizar_dados_instrutor/<int:user_id>', views.atualizar_dados_instrutor, name='atualizar_dados_instrutor'),
    path('atualizar_dados_treino/<int:user_id>', views.atualizar_dados_treino, name='atualizar_dados_treino'),
    path('deletar_aluno/<int:user_id>', views.deletar_aluno, name="deletar_aluno"),
    path('deletar_instrutor/<int:user_id>', views.deletar_instrutor, name="deletar_instrutor"),
    path('deletar_treino/<int:user_id>', views.deletar_instrutor, name="deletar_treino"),
    path('deletar_turma/<int:user_id>', views.deletar_instrutor, name="deletar_turma")


]