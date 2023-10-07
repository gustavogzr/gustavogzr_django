from django.shortcuts import render
from .models import tarefa, responsavel_tarefa

# Create your views here.

from datetime import date

def listar_tarefas(request):
    print(tarefa.objects.get(id=1).data_conclusao_prevista)
    contexto = {
        'tarefas': tarefa.objects.filter(data_conclusao_prevista=date.today()).order_by('data_conclusao_prevista'),
    }
    return render(request, 'listar_tarefas.html', contexto)
