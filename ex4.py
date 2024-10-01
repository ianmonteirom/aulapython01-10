"""
4. A API abaixo retorna um JSON com as informações de 100 produtos. Faça um
programa que consulte a API e informe o valor total do estoque (somatório de todos
os produtos). Considere que cada produto possui um preço (price), um desconto
(discountPercentage) que deve ser aplicado ao preço de cada produto e uma
quantidade de itens em estoque (stock).
https://dummyjson.com/products?limit=100
"""

import requests
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

try:
    response = requests.get(f'http://dummyjson.com/products?limit=100')
    if response.status_code == 200:
        dados = response.json()
        valor_total_estoque = 0
        for i in range(len(dados['products'])):
            valor_produto_estoque = (((dados['products'][i]['price'] *
                                       dados['products'][i]['discountPercentage']) / 100)
                                     * dados['products'][i]['stock'])

            valor_total_estoque += valor_produto_estoque

    else:
        print('Erro de requisição')


except requests.exceptions.ConnectionError:
    print('Erro de requisição')

valor_total_estoque = locale.format_string("%.2f", valor_total_estoque, grouping=True)
print(f'VALOR TOTAL DO ESTOQUE: R${valor_total_estoque}')
