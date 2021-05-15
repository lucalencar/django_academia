from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK
from .models import Aluno, Instrutor, Treino, Turma
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def inicio(request):

    alunos = Aluno.objects.all()
    instrutor = Instrutor.objects.all()
    treinos = Treino.objects.all()
    turmas = Turma.objects.all()


    contexto = {
        'alunos': alunos,
        'instrutor': instrutor,
        'treinos': treinos,
        'turmas': turmas
    }

    return render(request, 'inicio.html', contexto)


def form_cadastro_aluno(request):
    return render(request, 'cadastro_aluno.html')

def form_cadastro_instrutor(request):
    return render(request, 'cadastro_instrutor.html')

def form_cadastro_turma(request):
    return render(request, 'cadastro_turma.html')

def form_cadastro_treino(request):

    return render(request, 'cadastro_treino.html')

def visualizar_aluno(request, user_id):

    if request.method == 'GET':
        alunos = Aluno.objects.filter(id=user_id)

        contexto = {
            'alunos': alunos
        }
    return render(request, 'visualizar_aluno.html', contexto)

def visualizar_instrutor(request, user_id):

    if request.method == 'GET':
        instrutor = Instrutor.objects.filter(id=user_id)

        contexto = {
            'instrutor': instrutor
        }
    return render(request, 'visualizar_instrutor.html', contexto)

def visualizar_treino(request, user_id):

    if request.method == 'GET':
        treinos = Treino.objects.filter(id=user_id)

        contexto = {
            'treinos': treinos
        }
    return render(request, 'visualizar_treino.html', contexto)

def visualizar_turma(request, user_id):

    if request.method == 'GET':
        turmas = Turma.objects.filter(id=user_id)

        contexto = {
            'turmas': turmas
        }
    return render(request, 'visualizar_turma.html', contexto)


def atualizar_dados_aluno(request, user_id):

    if request.method == 'GET':
        alunos = Aluno.objects.filter(id=user_id)
        
        contexto = {
            'alunos': alunos
        }

        return render(request, "atualizar_aluno.html", contexto)


def atualizar_dados_treino(request, user_id):
    treinos = Treino.objects.filter(id=user_id)

    contexto = {
        'treinos': treinos
    }

    return render(request, "atualizar_treino.html", contexto)

def atualizar_dados_turma(request, user_id):
    turma = Turma.objects.filter(id=user_id)

    contexto = {
        'turma': turma
    }
    return render(request, "atualizar_turma.html", contexto)
    

def atualizar_alunos(request):
    if request.method == 'POST':
        
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        endereco = request.POST.get('endereco')
        cep =request.POST.get('cep')
        bairro = request.POST.get('bairro')
        data_matricula = request.POST.get('data_matricula')
        estado = request.POST.get('estado')
        genero = request.POST.get('genero')
        data_nascimento = request.POST.get('data_nascimento')
        user_id = request.POST.get('user_id')

        alunos = Aluno.objects.filter(id=user_id)
        alunos.update(nome=nome, sobrenome=sobrenome, cpf=cpf, telefone=telefone, peso=peso, altura=altura, genero=genero, bairro=bairro, data_matricula=data_matricula, data_nascimento=data_nascimento, estado=estado, endereco=endereco, cep=cep)

        return HttpResponseRedirect('/sistema/inicio')

def atualizar_dados_instrutor(request, user_id):

    if request.method == 'GET':

        instrutor = Instrutor.objects.filter(id=user_id)

        contexto = {
            'instrutor': instrutor
        }

        return render(request, 'atualizar_instrutor.html', contexto)

def atualizar_instrutor(request):
    if request.method == 'POST':
        
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        titulacao = request.POST.get('titulacao')
        genero = request.POST.get('genero')
        user_id = request.POST.get('user_id')

        instrutor = Instrutor.objects.filter(id=user_id)
        instrutor.update(titulacao=titulacao, nome=nome, sobrenome=sobrenome, cpf=cpf, telefone=telefone, genero=genero)

        return HttpResponseRedirect('/sistema/inicio')

def atualizar_treino(request):
    if request.method == 'POST':

        rotina = request.POST.get('rotina')
        hora_inicio_treino = request.POST.get('hora_inicio_treino')
        hora_fim_treino = request.POST.get('hora_fim_treino')
        data_treino = request.POST.get('data_treino')
        cod_instrutor = request.POST.get('cod_instrutor')
        cod_aluno = request.POST.get('cod_aluno')
        user_id = request.POST.get('user_id')

        treino = Treino.objects.filter(id=user_id)
        treino.update(rotina=rotina, hora_fim_treino=hora_fim_treino, hora_inicio_treino=hora_inicio_treino, data_treino=data_treino, cod_instrutor=cod_instrutor, cod_aluno=cod_aluno)

        return HttpResponseRedirect('/sistema/inicio')

def atualizar_turma(request):
    if request.method == 'POST':

        atividade = request.POST.get('atividade')
        hora_inicio_turma = request.POST.get('hora_inicio_turma')
        hora_fim_turma = request.POST.get('hora_fim_turma')
        data_turma = request.POST.get('data_turma')
        instrutor = request.POST.get('instrutor')
        user_id = request.POST.get('user_id')

        turma = Turma.objects.filter(id=user_id)
        turma.update(atividade=atividade, hora_inicio_turma=hora_inicio_turma, hora_fim_turma=hora_fim_turma, data_turma=data_turma, instrutor=instrutor)

        return HttpResponseRedirect('/sistema/inicio')

def deletar_aluno(request, user_id):

    if request.method == 'GET':
        alunos = Aluno.objects.filter(id=user_id)
        alunos.delete()

    return HttpResponseRedirect('/sistema/inicio')

def deletar_instrutor(request, user_id):

    if request.method == 'GET':
        instrutor = Instrutor.objects.filter(id=user_id)
        instrutor.delete()
    
    return HttpResponseRedirect('/sistema/inicio')

def deletar_treino(request, user_id):

    if request.method == 'GET':
        treinos = Treino.objects.filter(id=user_id)
        treinos.delete()
    
    return HttpResponseRedirect('/sistema/inicio')

def deletar_turma(request, user_id):

    if request.method == 'GET':
        turmas = Turma.objects.filter(id=user_id)
        turmas.delete()
    
    return HttpResponseRedirect('/sistema/inicio')

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
        aluno.telefone = request.POST.get('telefone')
        aluno.save()


    return HttpResponseRedirect('/sistema/inicio')  

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


    return HttpResponseRedirect('/sistema/inicio')

def cadastro_treino(request):
    

    if request.method == 'POST':
        treino = Treino()
        treino.rotina = request.POST.get('rotina')
        treino.hora_inicio_treino = request.POST.get('hora_inicio_treino')
        treino.hora_fim_treino = request.POST.get('hora_fim_treino')
        treino.data_treino = request.POST.get('data_treino')   
        treino.cod_aluno = request.POST.get('cod_aluno')
        treino.cod_instrutor = request.POST.get('cod_instrutor')
        treino.save()


    return HttpResponseRedirect('/sistema/inicio')

def cadastro_turma(request):

    if request.method == 'POST':

        turma = Turma()
        turma.atividade = request.POST.get('atividade')
        turma.hora_inicio_turma = request.POST.get('hora_inicio_turma')
        turma.hora_fim_turma = request.POST.get('hora_fim_turma')
        turma.data_turma = request.POST.get('data_turma')
        turma.alunos = request.POST.get('alunos')
        turma.instrutor = request.POST.get('instrutor')

    return HttpResponseRedirect('/sistema/inicio')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return HttpResponseRedirect('/sistema/inicio')
    else:
        form_usuario = UserCreationForm()

    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return HttpResponseRedirect('/sistema/inicio')
        else:
            messages.error(request,'username ou senha incorretos!')
            return HttpResponseRedirect('/sistema/logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})


def deslogar_usuario(request):
    logout(request)
    return HttpResponseRedirect('/sistema/inicio')

