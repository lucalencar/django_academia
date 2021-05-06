from django.db import models

# Create your models here.

class Aluno(models.Model):

    nome = models.CharField(
        max_length = 200,
        null = False,
        blank = False
    )
    sobrenome = models.CharField(
        max_length = 200,
        null = False,
        blank = False
    )

    data_nascimento = models.DateField(
        null = True,
        blank = True
    )
    
    telefone = models.CharField(
        max_length = 14,
        null = False,
        blank = False
    )

    cpf = models.CharField(
        max_length = 14,
        null = False,
        blank = False
    )


    endereco = models.CharField(
        max_length = 200,
        null = False,
        blank = False        
    )

    bairro = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        default=None          
    )

    cep = models.CharField(
        max_length = 9,
        null = False,
        blank = False         
    )

    cidade = models.CharField(
        max_length = 100,
        null = False,
        blank = False         
    )

    estado = models.CharField(
        max_length = 2,
        null = False,
        blank = False         
    )

    peso = models.CharField(
        max_length = 3,
        null = False,
        blank = False
    )

    altura = models.CharField(
        max_length = 4,
        null = False,
        blank = False
    )

    data_matricula = models.DateField(
        null = True,
        blank = True
    )

    genero_choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outro")
    )

    genero = models.CharField(
        max_length = 1,
        choices = genero_choices,
        null = True,
        blank = True
    )

    objects = models.Manager()



class Instrutor(models.Model):

    titulacao = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    nome = models.CharField(
        max_length = 200,
        null = False,
        blank = False
    )
    sobrenome = models.CharField(
        max_length = 200,
        null = False,
        blank = False
    )

    telefone = models.CharField(
        max_length = 14,
        null = False,
        blank = False
    )

    cpf = models.CharField(
        max_length = 14,
        null = False,
        blank = False
    )

    genero_choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outro")
    )

    genero = models.CharField(
        max_length = 1,
        choices = genero_choices,
        null = True,
        blank = True
    )

    objects = models.Manager()
    

class Treino(models.Model):

    hora_inicio_treino = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = True
    )

    hora_fim_treino = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = True
    )

    data_treino = models.DateField(
        null = True,
        blank = True
    )

    rotina = models.CharField(
        max_length = 500,
        null = False,
        blank = False
    )

    cod_instrutor = models.OneToOneField(
        'Instrutor',
        on_delete = models.CASCADE,
        related_name = '+',
        null = True,
        blank = True

    )

    cod_aluno = models.OneToOneField(
        'Aluno',
        on_delete = models.CASCADE,
        related_name = '+',
        null = True,
        blank = True
    )

    objects = models.Manager()    

class Turma(models.Model):

    atividade = models.CharField(
        max_length = 300,
        null = False,
        blank = False
    )

    hora_inicio_turma = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = True
    )

    hora_fim_turma = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = True
    )

    data_turma = models.DateField(
        null = True,
        blank = True
    )

    instrutor = models.OneToOneField(
        'Instrutor',
        on_delete = models.CASCADE,
        related_name = '+'
    )

    alunos = models.ManyToManyField(
        'Aluno'
    )

    objects = models.Manager()

    