from api.schemas.ifpimon_schema import IFPIMonSchema


class InMemoryIFPIMonRepository:
    # Ao iniciar, o repositorio já começa possuindo os ifpimons
    # Esse underline em "_ifpimons" é aviso informal de que o atributo deve ser usado somente dentro da classe
    def __init__(self) -> None:
        self._ifpimons: list[IFPIMonSchema] = [
            IFPIMonSchema(
                id=1,
                nome="Celtamon",
                tipo="Metal",
                treinador="Vitor",
                image_url="/public/ifpimons/celtamon.webp",
                descricao="Clássica referência.."
            ),
            IFPIMonSchema(
                id=2,
                nome="GPTmon",
                tipo="Elétrico",
                treinador="Gabriel",
                image_url="/public/ifpimons/gptmon.webp",
                descricao="Ele sabe de mais..."
            ),
            IFPIMonSchema(
                id=3,
                nome="Bombomon",
                tipo="Objeto",
                treinador="Geovany",
                image_url="/public/ifpimons/bombomon.webp",
                descricao="Objeto ou Método?"
            )
        ]
    # Esse metodo e responsavel por procurar a um ifpimon por id, retorna o objeto se encontrado caso contrario retorna "None"
    def get_by_id(self, ifpimon_id: int) -> IFPIMonSchema | None:
        return next(
            (
            ifpimon
            for ifpimon in self._ifpimons
            if ifpimon.id == ifpimon_id
            ),
            None
        )
    # Esse metodo e responavel por devolver a lista de ifpimons
    def get_all(self) -> list[IFPIMonSchema]:
        return self._ifpimons
