# Caso de uso responsavel por retornar um ifpimon por id
from api.repositories.ifpimon_repository import IFPIMonRepository
from api.schemas.ifpimon_schema import IFPIMonSchema
from api.exceptions.ifpimon_exceptions import IFPIMonNotFoundError


class GetIFPIMonById:
    def __init__(self, repository: IFPIMonRepository):
        self.repository = repository

    def execute(self, ifpimon_id: int) -> IFPIMonSchema:
        # O ifpimon pode ou não existir
        ifpimon = self.repository.get_by_id(ifpimon_id)

        # Caso ele não exista, ele é direcionado para a classe de erros
        if ifpimon is None:
            raise IFPIMonNotFoundError(ifpimon_id)

        return ifpimon
