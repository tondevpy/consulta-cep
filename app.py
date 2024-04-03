import requests

cep = input('Informe o CEP que deseja pesquisar: ')
cep = cep.replace(' ', '')
cep = cep.replace('-', '')

url = f'https://viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

try:
    if response.status_code == 200:
        data = response.json()
        cep = data['cep']
        rua = data['logradouro']
        bairro = data['bairro']
        cidade = data['localidade']
        uf = data['uf']

        retorno = f"\nEndereço\n\nRua: {rua}\nBairro: {bairro}\nCidade: {cidade}\nCEP: {cep}"
        
        print('CEP localizado')
        print(retorno)

    else:
        print('Informou um CEP inválido')
except requests.exceptions.HTTPError:
    print('Erro ao fazer a requisição HTTP.')
except requests.exceptions.RequestException as e:
    print('Ocorreu um erro durante a requisição:', e)
except KeyError:
    print('CEP não encontrado ou formato de resposta inválido.')
except Exception as e:
    print('Ocorreu um erro inesperado:', e)