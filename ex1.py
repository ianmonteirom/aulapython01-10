"""
1. Solicite ao usuário a sigla de uma UF e utilize a API abaixo para consultar e exibir os
nomes de todos os municípios da UF informada.
https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios
"""

import requests

uf = str(input('Digite o UF: '))

try:
    response = requests.get(f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')
    if response.status_code == 200:
        dados = response.json()
        print(f'MUNICÍPIOS DE {uf.upper()}')
        print('--' * 40)
        for i in range(len(dados)):
            print(f'Município {i + 1}: {dados[i]["nome"]}')
    else:
        print('Erro de requisição')


except requests.exceptions.ConnectionError:
    print('Erro de requisição')
except Exception:
    print('Erro.')
