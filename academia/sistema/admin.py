from django.contrib import admin
from .models import Aluno
from .models import Instrutor
from .models import Treino
from .models import Turma

admin.site.register(Aluno)
admin.site.register(Instrutor)
admin.site.register(Treino)
admin.site.register(Turma)

