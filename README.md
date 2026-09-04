# IFPI Mon API

## Revisores

As principais revisões e aprovações do projeto são realizadas por:

| Revisor | Perfil no GitHub |
|---|---|
| Mailson Sousa | [@MailsonSousa88](https://github.com/MailsonSousa88) |
| Roger Pierre | [@RogerPierre](https://github.com/RogerPierre) |
| Rikelry Souza | [@Rikelry](https://github.com/Rikelry) |

API de consulta dos IFPI Mons, desenvolvida em Python com FastAPI como parte
da disciplina de Programação para Internet II.

O projeto usa uma arquitetura em camadas para separar as rotas HTTP, os
controllers, os casos de uso e o acesso aos dados. Atualmente, é possível
listar todos os IFPI Mons e buscar um deles pelo ID.

## Tecnologias

- Python 3.12 ou superior;
- FastAPI;
- Pydantic;
- uv para gerenciamento do ambiente e das dependências.

## Armazenamento dos dados

A versão atual não utiliza um banco de dados externo. Os IFPI Mons são dados
mockados, mantidos em memória enquanto a aplicação está em execução. Ao
reiniciar o servidor, os dados retornam ao estado inicial.

O acesso aos dados é definido pelo contrato `IFPIMonRepository`. A
implementação atual é `InMemoryIFPIMonRepository`, permitindo que, no futuro,
o armazenamento seja substituído por um banco real sem alterar as rotas, os
controllers ou os casos de uso.

## Requisitos

- [Python 3.12+](https://www.python.org/downloads/);
- [uv](https://docs.astral.sh/uv/).

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/MailsonSousa88/ifpiMonAPI.git
cd ifpiMonAPI
uv sync
```

## Execução

Inicie o servidor de desenvolvimento na raiz do projeto:

```bash
uv run fastapi dev api/main.py
```

A API ficará disponível em `http://127.0.0.1:8000`. A documentação interativa
do FastAPI poderá ser acessada em `http://127.0.0.1:8000/docs`.

## Endpoints atuais

| Método | Caminho | Descrição |
|---|---|---|
| `GET` | `/` | Apresenta informações e links da API |
| `GET` | `/api/ifpimons` | Lista todos os IFPI Mons |
| `GET` | `/api/ifpimons/{ifpimon_id}` | Busca um IFPI Mon pelo ID |

Quando o ID informado não existe, a API responde com o status `404` e uma
mensagem produzida pelo handler centralizado de exceções.

## Arquitetura

```text
api/
├── main.py
├── dependencies.py
├── controllers/
├── exceptions/
├── repositories/
├── routes/
├── schemas/
├── services/
└── usecases/
```

Responsabilidade resumida de cada camada:

- **routes:** define os endpoints e recebe as requisições HTTP;
- **controllers:** coordena a chamada dos casos de uso;
- **usecases:** implementa as ações e regras da aplicação;
- **services:** reserva capacidades externas ou compartilhadas;
- **repositories:** define o contrato e o acesso aos dados;
- **schemas:** define e valida os formatos dos dados;
- **exceptions:** centraliza erros conhecidos e seus handlers HTTP;
- **dependencies.py:** cria e conecta repository, casos de uso e controller;
- **main.py:** inicializa o FastAPI, registra os handlers e inclui as rotas.

Consulte a documentação detalhada:

- [Arquitetura da API](docs/api/arquitetura.md);
- [Funcionamento da API](docs/api/funcionamento.md);
- [Catálogo atual](docs/wiki/catalogo.md).

## Testes

Execute os testes automáticos com:

```bash
uv run python -m unittest discover
```

## Contribuição

Antes de alterar o projeto, leia o [guia de contribuição](CONTRIBUTING.md). Ao
criar uma issue ou um pull request, utilize os templates disponíveis no
repositório.
