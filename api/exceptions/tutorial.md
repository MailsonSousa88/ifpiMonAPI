# Tutorial: tratamento centralizado de erros com FastAPI

Este tutorial ensina a criar um tratamento centralizado para o erro de IFPI Mon
não encontrado. Ele parte do código atual do projeto e explica cada alteração
necessária.

Ao terminar, uma requisição para um ID inexistente deverá produzir:

```http
GET /ifpimonapi/ifpimons/999
```

```json
{
  "error": "ifpimon_not_found",
  "message": "IFPI Mon com ID 999 não foi encontrado."
}
```

com o status HTTP `404 Not Found`.

## 1. Fluxo que será construído

```text
Route recebe o ID
    ↓
Controller chama o use case
    ↓
Use case consulta o repository
    ↓
Repository devolve None
    ↓
Use case lança IFPIMonNotFoundError
    ↓
FastAPI encontra o handler registrado
    ↓
Handler devolve JSON com status 404
```

Não será necessário colocar `try/except` na route, no controller ou nesse use
case. O FastAPI já captura a exceção lançada e a envia ao handler correspondente.

## 2. Estrutura dos arquivos

```text
api/
├── exceptions/
│   ├── __init__.py
│   ├── ifpimon_exceptions.py
│   ├── handlers.py
│   └── tutorial.md
├── usecases/
│   └── get_ifpimon_by_id.py
├── routes/
│   └── ifpimon_routes.py
└── main.py
```

Cada arquivo terá uma responsabilidade:

| Arquivo | Responsabilidade |
|---|---|
| `ifpimon_exceptions.py` | Declarar os tipos de erro relacionados a IFPI Mons |
| `handlers.py` | Transformar esses erros em respostas HTTP |
| `get_ifpimon_by_id.py` | Detectar que o IFPI Mon não existe e lançar o erro |
| `main.py` | Registrar os handlers na aplicação FastAPI |

## 3. Criar a exceção personalizada

Abra:

```text
api/exceptions/ifpimon_exceptions.py
```

O nome atual `IFPIMonFoundError` significa “erro de IFPI Mon encontrado”. Como o
erro representa um resultado **não encontrado**, utilize
`IFPIMonNotFoundError`:

```python
class IFPIMonNotFoundError(Exception):
    def __init__(self, ifpimon_id: int):
        self.ifpimon_id = ifpimon_id
        super().__init__(
            f"IFPI Mon com ID {ifpimon_id} não foi encontrado."
        )
```

Explicação linha por linha:

```python
class IFPIMonNotFoundError(Exception):
```

Cria um novo tipo de erro que herda da classe `Exception` do Python.

```python
def __init__(self, ifpimon_id: int):
```

É o construtor da exceção. Ele recebe o ID que não foi encontrado.

```python
self.ifpimon_id = ifpimon_id
```

Guarda o ID dentro do objeto de erro. O handler poderá acessá-lo posteriormente
com `error.ifpimon_id`.

```python
super().__init__(...)
```

Inicializa a parte padrão de `Exception` com uma mensagem. Isso ajuda em logs e
durante a depuração.

Importante: `IFPIMonNotFoundError(ifpimon_id)` não devolve o ID ao usuário. Ele
cria um objeto de erro que guarda o ID como informação.

## 4. Lançar a exceção no use case

Abra:

```text
api/usecases/get_ifpimon_by_id.py
```

Troque o import antigo pelo novo nome:

```python
from api.exceptions.ifpimon_exceptions import IFPIMonNotFoundError
```

O use case completo deve ficar com este comportamento:

```python
from api.exceptions.ifpimon_exceptions import IFPIMonNotFoundError
from api.repositories.ifpimon_repository import IFPIMonRepository
from api.schemas.ifpimon_schema import IFPIMonSchema


class GetIFPIMonById:
    def __init__(self, repository: IFPIMonRepository):
        self.repository = repository

    def execute(self, ifpimon_id: int) -> IFPIMonSchema:
        ifpimon = self.repository.get_by_id(ifpimon_id)

        if ifpimon is None:
            raise IFPIMonNotFoundError(ifpimon_id)

        return ifpimon
```

Antes dessa mudança, o método podia devolver:

```text
IFPIMonSchema ou None
```

Agora existem dois caminhos:

```text
Encontrou     → devolve IFPIMonSchema
Não encontrou → lança IFPIMonNotFoundError
```

Por isso, o tipo de retorno do método passa a ser somente:

```python
def execute(self, ifpimon_id: int) -> IFPIMonSchema:
```

O `raise` interrompe a execução. Se ele for executado, o último `return` não será
alcançado.

## 5. Criar o handler HTTP

Abra:

```text
api/exceptions/handlers.py
```

Apague o import incompleto:

```python
from fast
```

Depois escreva:

```python
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.exceptions.ifpimon_exceptions import IFPIMonNotFoundError


async def ifpimon_not_found_handler(
    request: Request,
    error: IFPIMonNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={
            "error": "ifpimon_not_found",
            "message": (
                f"IFPI Mon com ID {error.ifpimon_id} "
                "não foi encontrado."
            ),
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        IFPIMonNotFoundError,
        ifpimon_not_found_handler,
    )
```

### Imports do handler

```python
from http import HTTPStatus
```

`HTTPStatus` pertence à biblioteca padrão do Python. Não precisa ser instalado.
`HTTPStatus.NOT_FOUND` representa o código `404`.

```python
from fastapi import FastAPI, Request
```

- `FastAPI` é utilizado para registrar o handler;
- `Request` representa a requisição que estava sendo processada quando o erro
  aconteceu.

```python
from fastapi.responses import JSONResponse
```

`JSONResponse` já faz parte das dependências do FastAPI. Não é uma biblioteca
externa adicional. Ela é usada porque um handler personalizado precisa construir
e devolver uma resposta HTTP.

### Função do handler

```python
async def ifpimon_not_found_handler(
    request: Request,
    error: IFPIMonNotFoundError,
) -> JSONResponse:
```

O FastAPI chama essa função automaticamente quando encontra um
`IFPIMonNotFoundError`.

- `request` contém informações da requisição;
- `error` é o objeto criado pelo `raise` no use case;
- `error.ifpimon_id` contém o ID que não foi encontrado;
- `async` permite que o handler seja executado no fluxo assíncrono do FastAPI.

O parâmetro `request` ainda não é utilizado no corpo da função, mas faz parte da
assinatura esperada pelo mecanismo de handlers. Futuramente ele pode fornecer a
URL, o método HTTP ou outras informações para logs.

### Resposta produzida

```python
return JSONResponse(
    status_code=HTTPStatus.NOT_FOUND,
    content={...},
)
```

- `status_code` define o código HTTP;
- `content` define o JSON enviado ao cliente;
- `return` devolve a resposta criada pelo handler.

### Registro do handler

```python
app.add_exception_handler(
    IFPIMonNotFoundError,
    ifpimon_not_found_handler,
)
```

Essa instrução cria a associação:

```text
IFPIMonNotFoundError → ifpimon_not_found_handler
```

Sem esse registro, o FastAPI não saberá qual resposta personalizada deve criar
para a exceção.

## 6. Registrar os handlers no `main.py`

Abra:

```text
api/main.py
```

Adicione o import:

```python
from api.exceptions.handlers import register_exception_handlers
```

Depois da criação do `app`, registre os handlers:

```python
app = FastAPI()

register_exception_handlers(app)
```

O registro precisa receber a mesma instância de `FastAPI` que será executada pelo
servidor.

O começo do arquivo ficará semelhante a:

```python
from fastapi import FastAPI

from api.exceptions.handlers import register_exception_handlers
from api.routes.ifpimon_routes import router as ifpimon_routes
from api.routes.root_routes import router as ifpimon_root_router


app = FastAPI()

register_exception_handlers(app)
```

Os routers podem continuar sendo incluídos depois desse trecho.

## 7. Manter a route simples

A route não precisa de `try/except` nem de `HTTPException` para esse erro:

```python
@router.get(
    "/{ifpimon_id}",
    response_model=IFPIMonSchema,
    status_code=HTTPStatus.OK,
)
def get_ifpimon_by_id(ifpimon_id: int):
    return ifpimon_controller.get_by_id_execute(ifpimon_id)
```

Imports necessários para esse exemplo:

```python
from http import HTTPStatus

from fastapi import APIRouter

from api.dependencies import ifpimon_controller
from api.schemas.ifpimon_schema import IFPIMonSchema
```

Se o use case lançar `IFPIMonNotFoundError`, a função da route será interrompida
e o FastAPI chamará o handler automaticamente.

## 8. Verificar o controller

O controller apenas repassa o ID ao use case:

```python
def get_by_id_execute(self, ifpimon_id: int) -> IFPIMonSchema:
    return self.get_ifpimon_by_id_UseCase.execute(ifpimon_id)
```

Como o use case agora devolve um IFPI Mon ou lança uma exceção, o retorno do
controller também não precisa mais incluir `None`.

Não coloque `try/except` no controller apenas para relançar o mesmo erro. Isso não
adicionaria nenhum comportamento útil.

## 9. Testar o funcionamento

Na raiz do projeto, execute:

```bash
uv run fastapi dev api/main.py
```

### ID existente

Acesse:

```http
GET http://127.0.0.1:8000/ifpimonapi/ifpimons/1
```

Resultado esperado:

```http
200 OK
```

```json
{
  "id": 1,
  "nome": "Pycatmon",
  "tipo": "Eletrico",
  "treinador": null
}
```

### ID inexistente

Acesse:

```http
GET http://127.0.0.1:8000/ifpimonapi/ifpimons/999
```

Resultado esperado:

```http
404 Not Found
```

```json
{
  "error": "ifpimon_not_found",
  "message": "IFPI Mon com ID 999 não foi encontrado."
}
```

### ID com formato inválido

Acesse:

```http
GET http://127.0.0.1:8000/ifpimonapi/ifpimons/abc
```

Como `ifpimon_id` foi declarado como `int`, o próprio FastAPI recusará o texto
`abc` e responderá com status `422`. Esse erro é tratado automaticamente pelo
FastAPI e não utiliza `IFPIMonNotFoundError`.

## 10. Onde entra o `try/except`?

Esse fluxo não precisa de `try/except`:

```python
if ifpimon is None:
    raise IFPIMonNotFoundError(ifpimon_id)
```

`None` é um valor retornado, não uma exceção. O `if` detecta esse valor e o
`raise` cria a exceção da aplicação.

O `try/except` será necessário quando uma operação realmente puder lançar uma
exceção que precisa ser convertida. Por exemplo, no futuro, uma biblioteca de
banco poderá lançar `DatabaseConnectionError`:

```python
try:
    return database.find_by_id(ifpimon_id)
except DatabaseConnectionError as error:
    raise RepositoryUnavailableError() from error
```

Nesse exemplo:

- `try` executa a consulta que pode falhar;
- `except` captura apenas o erro conhecido do banco;
- `raise` transforma o erro da biblioteca em um erro compreendido pela
  aplicação;
- `from error` preserva internamente a causa original.

Não use `except Exception` em todas as camadas. Isso pode esconder erros de
programação e dificultar a depuração.

## 11. Diferença para o exemplo com `HTTPException`

Na forma mais simples, a route pode fazer:

```python
if ifpimon is None:
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail="IFPI Mon não encontrado.",
    )
```

Nesse caso, o handler padrão do FastAPI constrói a resposta. Não é necessário
criar `handlers.py`.

Na forma centralizada deste tutorial:

```text
Use case lança uma exceção da aplicação
              ↓
Handler personalizado define a resposta HTTP
```

A vantagem é que use cases não precisam importar FastAPI e todas as respostas do
mesmo erro seguem um formato único.

## 12. Próximos erros

Depois que `IFPIMonNotFoundError` estiver funcionando, outros erros podem seguir
o mesmo padrão:

```text
IFPIMonAlreadyExistsError → 409 Conflict
InvalidIFPIMonDataError   → 400 Bad Request
RepositoryUnavailableError → 503 Service Unavailable
```

Não crie todos antecipadamente. Adicione cada exceção quando uma regra real da
aplicação precisar dela.

O FastAPI também possui `RequestValidationError` para erros de validação de
parâmetros e corpos de requisição. A personalização desse erro pode ser feita em
uma etapa posterior, depois que o primeiro handler estiver compreendido e
testado.

## 13. Checklist

- [ ] Renomeei `IFPIMonFoundError` para `IFPIMonNotFoundError`.
- [ ] Atualizei o import e o `raise` no use case.
- [ ] Removi `| None` do retorno do use case.
- [ ] Removi o import incompleto `from fast` de `handlers.py`.
- [ ] Criei `ifpimon_not_found_handler`.
- [ ] Criei `register_exception_handlers`.
- [ ] Registrei os handlers no `main.py`.
- [ ] Mantive a route sem `try/except` para esse caso.
- [ ] Testei um ID existente.
- [ ] Testei um ID inexistente.
- [ ] Testei um ID com formato inválido.

## Referência

- [Tratamento de erros — documentação oficial do FastAPI](https://fastapi.tiangolo.com/pt/tutorial/handling-errors/)
