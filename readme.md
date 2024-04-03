# Consulta de CEP via API

## Descrição

Este é um projeto simples que permite aos usuários consultar informações de endereço com base em um CEP fornecido. O projeto utiliza a API do ViaCEP para obter os dados de endereço associados a um determinado CEP.

## Funcionalidades

- Solicita ao usuário que insira um CEP.
- Realiza uma requisição GET para a API do ViaCEP, fornecendo o CEP informado pelo usuário.
- Processa os dados de resposta JSON fornecidos pela API e extrai informações como rua, bairro, cidade e estado.
- Exibe o endereço completo encontrado com base no CEP fornecido.

## Pré-requisitos

Antes de executar o script, certifique-se de ter a biblioteca `requests` instalada. Você pode instalar a biblioteca utilizando o seguinte comando:

pip install requests

## Como usar

1. Execute o script `consulta_cep.py`.
2. Quando solicitado, insira o CEP que deseja pesquisar.
3. Aguarde o resultado da consulta. Se o CEP for válido, o endereço correspondente será exibido. Se o CEP for inválido ou não puder ser encontrado, uma mensagem de erro será exibida.

## Exemplo de Uso

Informe o CEP que deseja pesquisar: 01311-000
CEP localizado

Endereço

Rua: Avenida Paulista
Bairro: Bela Vista
Cidade: São Paulo
CEP: 01311-000

## Limitações

Este projeto depende da disponibilidade e precisão dos dados fornecidos pela API do ViaCEP. Se a API estiver indisponível ou retornar dados incorretos, os resultados da consulta podem ser afetados.

## Autor

[TonDevPy]

## Contribuição

Contribuições são bem-vindas! Se você encontrar bugs, problemas de desempenho ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
