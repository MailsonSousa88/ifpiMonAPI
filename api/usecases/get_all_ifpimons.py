# Caso de uso responsavel por retornar todos os ifpimons
from api.repositories.ifpimon_repository import IFPIMonRepository
from api.schemas.ifpimon_schema import IFPIMonSchema

class GetAllIFPIMons:
    def __init__(self, repository: IFPIMonRepository):
        self.repository = repository

    def execute(self) -> list[IFPIMonSchema]:
        return self.repository.get_all()