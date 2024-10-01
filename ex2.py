"""
2. Utilize a API abaixo para gerar uma listagem com os nomes de N usuários. Exiba a
lista em ordem alfabética
https://randomuser.me/api/?results={n}
"""

import requests

n = int(input('Quantidade de usuários: '))

try:
    response = requests.get(f'http://randomuser.me/api/?results={n}')
    if response.status_code == 200:
        dados = response.json()
        nomes = []
        for i in range(len(dados['results'])):
            print(dados['results'][i]['name']['first'])
            nomes.append(dados['results'][i]['name']['first'])
    else:
        print('Erro de requisição')


except requests.exceptions.ConnectionError:
    print('Erro de requisição')

nomes.sort()
print(f'Nomes dos primeiros {n} usuários: {nomes}')
