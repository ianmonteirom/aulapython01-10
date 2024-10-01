"""
3. A API abaixo retorna um JSON com informações de 50 receitas culinárias. Faça um
programa que consulte a API e exiba todas as receitas que utilizam um determinado
ingrediente informado pelo usuário.
https://dummyjson.com/recipes?limit=50
"""

import requests

try:
    response = requests.get(f'https://dummyjson.com/recipes?limit=50')
    if response.status_code == 200:
        dados = response.json()
        ingrediente = str(input('Digite um ingrediente: '))
        for i in range(len(dados['recipes'])):
            if ingrediente in dados['recipes'][i]['ingredients']:
                print(f'{ingrediente} é utilizado na receita {dados['recipes'][i]['name']}')
    else:
        print('Erro de requisição')


except requests.exceptions.ConnectionError:
    print('Erro de requisição')

