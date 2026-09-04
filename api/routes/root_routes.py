from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "name": "IFPIMon API",
        "docs": "/docs",
        "ifpimons": "/api/ifpimons",
        "ifpimon_by_id": "/api/ifpimons/1",
    }
