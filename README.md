# IFPI Mon API

API desenvolvida em Python como parte da disciplina de Programação para
Internet II. O projeto utilizará FastAPI e será construído com uma arquitetura
em camadas, separando o contrato HTTP, os casos de uso e o acesso aos dados.

> [!NOTE]
> O projeto está em sua estrutura inicial. Os endpoints e as regras de negócio
> ainda serão implementados.

## Tecnologias

- Python 3.12 ou superior;
- FastAPI;
- Pydantic;
- uv para gerenciamento do ambiente e das dependências.

## Armazenamento dos dados

A primeira versão não utilizará um banco de dados externo. Os IFPI Mons serão
dados mockados, mantidos em memória enquanto a aplicação estiver em execução.
Ao reiniciar o servidor, os dados retornarão ao estado inicial.

O acesso aos dados será feito por meio do contrato `IfpiMonRepository`. A
implementação inicial será `InMemoryIfpiMonRepository`, permitindo que, no
futuro, o armazenamento seja substituído por um banco real sem alterar as
rotas, os controllers ou os casos de uso.

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

## Execução atual

Enquanto a aplicação FastAPI ainda não foi criada, execute o ponto de entrada
inicial com:

```bash
uv run python api/main.py
```

Neste momento, o comando apenas confirma que o ambiente do projeto está
funcionando. O comando de inicialização do servidor será documentado quando a
instância do FastAPI for implementada.

## Arquitetura

```text
api/
├── main.py
├── controllers/
├── exceptions/
├── repositories/
├── routes/
├── schemas/
├── services/
└── usecases/
```

Responsabilidade resumida de cada camada:

- **routes:** define os endpoints e o contrato HTTP;
- **controllers:** coordena a entrada, a saída e a chamada dos casos de uso;
- **usecases:** implementa as ações e regras da aplicação;
- **services:** encapsula capacidades externas ou compartilhadas;
- **repositories:** define o contrato e as implementações de acesso aos dados;
- **schemas:** valida os dados de entrada e saída;
- **exceptions:** centraliza erros conhecidos e seus handlers HTTP.

Consulte a documentação detalhada:

- [Arquitetura da API](docs/api/arquitetura.md);
- [Funcionamento da API](docs/api/funcionamento.md).

## Estado do projeto

- [x] Estrutura inicial das camadas;
- [x] Documentação da arquitetura e do funcionamento;
- [x] Templates para issues e pull requests;
- [ ] Aplicação FastAPI;
- [ ] Entidades e schemas;
- [ ] Repository em memória com dados mockados;
- [ ] Casos de uso, controllers e rotas;
- [ ] Testes automatizados;
- [ ] Publicação no Render.

## Contribuição

Antes de alterar o projeto, leia o [guia de contribuição](CONTRIBUTING.md). Ao
criar uma issue ou um pull request, utilize os templates disponíveis no
repositório.
