from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    # return render(request, 'index.html')
   return render(request, 'index.html')

def consulta_api(request):
    url = f'https://viacep.com.br/ws/'
    formato = '/json/'
    ret = ''
    if 'buscar' in request.GET:
        cep = request.GET['buscar']
        data = requests.get(url+cep+formato)
        ret = data.json()
    dados = {}
    for key, value in enumerate (ret):
        dados[key] = value
    
    context = {
        'cep' : ret['cep'],
        'rua' : ret['logradouro'],
        'complemento' : ret['complemento'],
        'bairro' : ret['bairro'],
    }
    return render(request, 'resultado.html', context)

