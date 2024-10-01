import requests

cep = input('Informe o cep: ')

response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

try:
    if response.status_code == 200:
        dados = response.json()
        if 'erro' in dados:
            print('Erro. Cep inexistente')
        else:
            print(f'Rua: {dados["logradouro"]}\n'
                  f'UF: {dados["estado"]}')
    else:
        print('Erro de aquisição')
except requests.exceptions.ConnectionError:
    print('Erro de aquisição')