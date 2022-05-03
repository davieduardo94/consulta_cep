from django.http import HttpResponse
from django.shortcuts import render
import requests
import re


def index(request):
    # return render(request, 'index.html')
   return render(request, 'index.html')

def consulta_api(request):
    url = f'https://viacep.com.br/ws/'
    formato = '/json/'
    ret = ''
    dados = {}

    if 'buscar' in request.GET:
        cep = request.GET['buscar'].replace('-','')
        if len(cep) == 8:
            regex = r"^[0-9]+$"
            
            # realizando requisição na API com CEP informado
            data = requests.get(url+cep+formato)
            # recebendo dados no formato json
            ret = data.json()
        
            # percorrendo as key, values do json e transfornado em dict
            for key, value in enumerate (ret):
                dados[key] = value

            context = {
                'key_cep' : ret['cep'],
                'key_rua' : ret['logradouro'],
                'key_complemento' : ret['complemento'],
                'key_bairro' : ret['bairro'],
                'key_localidade' : ret['localidade'],
                'key_uf' : ret['uf'],
                'key_ddd' : ret['ddd'],
            }
    else:
        context  = {
            'result' : 'O CEP NÃO FOI ENCONTRADO OU NÃO INFORMADO CORRETAMENTE!'
        }
    
    return render(request, 'resultado.html', context)

