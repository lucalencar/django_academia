from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK
from .models import Aluno
from .models import Instrutor
from .models import Treino
from .models import Turma
# Create your views here.

'''
def form_cadastro(request):
    return render(request, 'cadastro.html')
'''


def cadastro_aluno(request):

    if request.method == 'POST':


        aluno = Aluno()
        aluno.nome=request.POST.get('nome')
        aluno.sobrenome = request.POST.get('sobrenome')
        aluno.endereco = request.POST.get('endereco')
        aluno.cep = request.POST.get('cep')
        aluno.genero = request.POST.get('genero')
        aluno.bairro = request.POST.get('bairro')
        aluno.cidade = request.POST.get('cidade')
        aluno.estado = request.POST.get('estado')
        aluno.cpf = request.POST.get('cpf')
        aluno.peso = request.POST.get('peso')
        aluno.altura = request.POST.get('altura')
        aluno.data_matricula = request.POST.get('data_matricula')
        aluno.save()
 
        response = {
            'response': HTTP_200_OK
        }

    return HttpResponse(json.dumps(response))   

def cadastro_instrutor(request):

    if request.method == 'POST':

        instrutor = Instrutor()
        instrutor.nome = request.POST.get('nome')
        instrutor.sobrenome = request.POST.get('sobrenome')
        instrutor.genero = request.POST.get('genero')
        instrutor.cpf = request.POST.get('cpf')
        instrutor.telefone = request.POST.get('telefone')
        instrutor.titulacao = request.POST.get('titulacao')
        instrutor.save()

        response = {
            'response': HTTP_200_OK
        }

    #return HttpResponseRedirect('/clientes/inicio')
    return HttpResponse(json.dumps(response))       


def cadastro_treino(request):

    if request.method == 'POST':

        treino = Treino()
        treino.rotina = request.POST.get('rotina')
        treino.hora_inicio = request.POST.get('hora_inicio')
        treino.hora_fim = request.POST.get('hora_fim')
        treino.data_treino = request.POST.get('data_treino')
        treino.cod_aluno = request.POST.get('cod_aluno')
        treino.cod_instrutor = request.POST.get('cod_instrutor')
        treino.save()

        response = {
            'response': HTTP_200_OK
        }

    return HttpResponse(json.dumps(response))

def cadastro_turma(request):

    if request.method == 'POST':

        turma = Turma()
        turma.atividade = request.POST.get('atividade')
        turma.hora_inicio_turma = request.POST.get('hora_inicio_turma')
        turma.hora_fim_turma = request.POST.get('hora_fim_turma')
        turma.data_turma = request.POST.get('data_turma')
        turma.alunos = request.POST.get('alunos')
        turma.instrutor = request.POST.get('instrutor')
    
        response = {
            'response': HTTP_200_OK
        }

    return HttpResponse(json.dumps(response))