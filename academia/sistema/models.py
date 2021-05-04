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
        null = False,
        blank = False
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

    data_nascimento = models.DateField(
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
        null = False,
        blank = False
    )

    objects = models.Manager()
    

class Treino(models.Model):

    hora_inicio_treino = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = False
    )

    hora_fim_treino = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = False
    )

    data_treino = models.DateField(
        null = False,
        blank = False
    )

    rotina = models.CharField(
        max_length = 500,
        null = False,
        blank = False
    )

    cod_instrutor = models.OneToOneField(
        'Instrutor',
        on_delete = models.CASCADE,
        related_name = '+'
    )

    cod_aluno = models.OneToOneField(
        'Aluno',
        on_delete = models.CASCADE,
        related_name = '+'
    )

    objects = models.Manager()    

class Turma(models.Model):

    atividade = models.CharField(
        max_length = 300,
        null = False,
        blank = False
    )

    alunos = models.ManyToManyField(
        'Aluno',
        related_name = '+'
    )

    hora_inicio_turma = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = False
    )

    hora_fim_turma = models.TimeField(
        auto_now = False,
        auto_now_add = False,
        null = False
    )

    data_turma = models.DateField(
        null = False,
        blank = False
    )

    instrutor = models.OneToOneField(
        'Instrutor',
        on_delete = models.CASCADE,
        related_name = '+'
    )

    objects = models.Manager()
