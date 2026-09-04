# REPRESENTA O CONTRATO QUE DEVE SER SEGUIDO POR CADA REPOSITÓRIO
from typing import Protocol, runtime_checkable
from api.schemas.ifpimon_schema import IFPIMonSchema

# Runtime checkable é útil para garantir que outras classes seguem o contrato definido em tempo de execução, procure mais sobre isinstance() se quiser entender melhor
@runtime_checkable
class IFPIMonRepository(Protocol):
    # Devolve um IFPIMon a partir de um ID
    def get_by_id(self, ifpimon_id: int) -> IFPIMonSchema | None:
        ...

    # Devolve uma lista de IFPIMons
    def get_all(self) -> list[IFPIMonSchema]:
        ...
