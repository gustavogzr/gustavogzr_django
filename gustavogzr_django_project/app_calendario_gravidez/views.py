from django.shortcuts import render
import datetime

# Create your views here.
# criar view calendario_gravidez com template 'calendario_gravidez.html'

def calendario_gravidez(request):
    # criar variavel data_ultima_menstruacao com valor de 30/06/2023
    data_ultima_menstruacao = datetime.date(2023, 6, 30)
    # criar variavel data_atual com data atual
    data_atual = datetime.date.today()
    # criar variavel qtde_semanas arrendondando para baixo (data atual - data_ultima_menstruacao)
    qtde_semanas = (data_atual - data_ultima_menstruacao).days // 7
    qtde_dias = (data_atual - data_ultima_menstruacao).days % 7
    # calculiar data_provavel_parto com data_ultima_menstruacao + 280 dias
    data_provavel_parto = data_ultima_menstruacao + datetime.timedelta(days=280)
    # criar dicionário "contexto" com as variáveis data_ultima_menstruacao e qtde_semanas
    contexto = {
        'dum': data_ultima_menstruacao,
        'semanas': qtde_semanas,
        'dias': qtde_dias,
        'dpp': data_provavel_parto
    }
    return render(request, 'calendario_gravidez.html', contexto)