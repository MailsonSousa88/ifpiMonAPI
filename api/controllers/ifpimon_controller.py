from api.schemas.ifpimon_schema import IFPIMonSchema
from api.usecases.get_all_ifpimons import GetAllIFPIMons
from api.usecases.get_ifpimon_by_id import GetIFPIMonById

class IFPIMonController:
    def __init__(self, get_all_UseCase: GetAllIFPIMons, get_ifpimon_by_id_UseCase: GetIFPIMonById):
        self.get_all_UseCase = get_all_UseCase
        self.get_ifpimon_by_id_UseCase = get_ifpimon_by_id_UseCase

    def get_all_execute(self) -> list[IFPIMonSchema]:
        return self.get_all_UseCase.execute()

    def get_by_id_execute(self, ifpimon_id: int) -> IFPIMonSchema:
        return self.get_ifpimon_by_id_UseCase.execute(ifpimon_id)