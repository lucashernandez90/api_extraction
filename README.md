# Gerenciamento de Feiras Livres 

Esta é uma API REST desenvolvida em Python com o framework Flask para a extração, 
consulta e gerenciamento dos dados oficiais das feiras livres da cidade de São Paulo (baseado nos dados do DEINFO_AB_FEIRASLIVRES_2014.csv).

Além disso utilizei PostMan para poder ter uma visualização melhor dos dados

---

# Instalar as depêndicias 

```
pip install -r requirements.txt
```

# Como Executar a API

Para iniciar o servidor local do Flask, execute o comando abaixo na raiz do projeto:

```
python src/main.py
```

O servidor ficará ativo e escutando requisições em `http://localhost:5000`

# Endpoints e Exemplos de Requisições/Respostas

Todas as respostas da API possuem o cabeçalho obrigatório `Content-Type: application/json.`

## 1. Listar Todas as Feiras

- Rota: ``Get /feiras`` 
- Exemplo de Resposta (Status 200 OK):

```JSON
[
  {
    "id": 1,
    "registro": "4041-0",
    "nome_feira": "VILA FORMOSA",
    "distrito": "VILA FORMOSA",
    "bairro": "VL FORMOSA",
    "regiao5": "Leste"
  }
]
```

## 2. Buscar Feira por ID Único

- Rota: ``GET /feiras/id/<id>``
- Exemplo de Resposta - Sucesso (Status 200 OK): ``GET /feiras/id/1``

``` JSON
{
  "id": 1,
  "registro": "4041-0",
  "nome_feira": "VILA FORMOSA",
  "distrito": "VILA FORMOSA",
  "bairro": "VL FORMOSA",
  "regiao5": "Leste"
}
```

- Exemplo de Resposta - Não Encontrado (Status 404 Not Found): ``GET /feiras/id/999999``

```JSON
{
  "erro": "no feiras found"
}
```

## 3. Buscar Feiras por Distrito

- Rota: ``GET /feiras/distrito/<nome_distrito>``
- Exemplo de Resposta - Sucesso (Status 200 OK): ``GET /feiras/distrito/VILA FORMOSA``

```JSON
[
  {
    "id": 1,
    "registro": "4041-0",
    "nome_feira": "VILA FORMOSA",
    "distrito": "VILA FORMOSA",
    "bairro": "VL FORMOSA",
    "regiao5": "Leste"
  }
]
```

## 4. Cadastrar Nova Feira 

- Rota: ``POST /feiras``
- Corpo da Requisição (JSON Payload):

```JSON
{
  "registro": "9999-TESTE",
  "nome_feira": "FEIRA DO POSTMAN",
  "distrito": "DISTRITO TESTE",
  "bairro": "BAIRRO TESTE",
  "regiao5": "Norte"
}
```

- Exemplo de Resposta - Sucesso (Status 201 Created):

```JSON
{
  "id": 881,
  "registro": "9999-TESTE",
  "nome_feira": "FEIRA DO POSTMAN",
  "distrito": "DISTRITO TESTE",
  "bairro": "BAIRRO TESTE",
  "regiao5": "Norte"
}
```

## 5. Atualizar Feira Existente

- Rota: ``PUT /feiras/registro/<codigo_registro>``
- Corpo da Requisição (JSON Payload): ``PUT /feiras/registro/9999-TESTE``

```JSON
{
  "nome_feira": "FEIRA ATUALIZADA",
  "bairro": "NOVO BAIRRO"
}
```

- Exemplo de Resposta - Sucesso (Status 200 OK):

```JSON
{
  "id": 881,
  "registro": "9999-TESTE",
  "nome_feira": "FEIRA ATUALIZADA",
  "distrito": "DISTRITO TESTE",
  "bairro": "NOVO BAIRRO",
  "regiao5": "Norte"
}
```

- Exemplo de Resposta - Bloqueio de Segurança (Status 400 Bad Request): (Se tentar alterar o código de registro protegido)

```JSON
{
  "erro": "cant modify registro"
}
```

## 6. Deletar Feira

- Rota: `DELETE /feiras/registro/<codigo_registro>`
- Exemplo de Resposta - Sucesso (Status 200 OK): `DELETE /feiras/registro/9999-TESTE`


```JSON
{
  "message": "feira 9999-TESTE deleted successfully"
}
```
- Exemplo de Resposta - Não Encontrada (Status 404 Not Found): `DELETE /feiras/registro/INVALIDO`

```JSON
{
  "erro": "feira not founded"
}
```

# Testes Automatizados e Cobertura

O projeto conta com uma suite de testes automatizados utilizando o pytest para garantir o funcionamento correto de todos os fluxos e regras de negócio da API.

## Como executar os testes simples:

```
pytest
```

## Como gerar a informação de cobertura de código (Terminal):

Para verificar a percentagem de linhas de código que estão protegidas por testes na pasta `src`, execute:

```
pytest --cov=src tests/
```

## Como gerar o Relatório Visual em HTML:

Para gerar uma documentação visual interativa da cobertura de testes, execute:

```
pytest --cov=src tests/ --cov-report=html
```
