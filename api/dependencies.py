# Esse arquivo centraliza as instâncias do projeto.
# O main.py fica responsável apenas por inicializar o sistema.
from api.controllers.ifpimon_controller import IFPIMonController
from api.usecases.get_ifpimon_by_id import GetIFPIMonById
from api.usecases.get_all_ifpimons import GetAllIFPIMons
from api.repositories.in_memory_ifpimon_repository import InMemoryIFPIMonRepository

# Lista de repositorios
repository = InMemoryIFPIMonRepository()

# Lista de casos de uso
get_all_use_case = GetAllIFPIMons(repository)
get_by_id = GetIFPIMonById(repository)

# Lista de controllers
ifpimon_controller = IFPIMonController(
    get_all_use_case,
    get_by_id
)

