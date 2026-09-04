from fastapi import APIRouter
from api.dependencies import ifpimon_controller

router = APIRouter(
    prefix="/ifpimons"
)

# CATEGORIA: GET

@router.get("", tags=["TODOS"])
def get_all_ifpimons():
    return ifpimon_controller.get_all_execute()

@router.get("/{ifpimon_id}", tags=["ID"])
def get_ifpimon_by_id(ifpimon_id:int):
    return ifpimon_controller.get_by_id_execute(ifpimon_id)