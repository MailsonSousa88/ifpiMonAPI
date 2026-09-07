# Base dos ifpiMons
# V1.0.0 - id, nome, tipo, treinador
from pydantic import BaseModel

# Modelo inicial (V1) dos IFPIMons
class IFPIMonSchema(BaseModel):
    id: int
    nome: str
    tipo: str
    descricao: str 
    treinador: str | None = None
    image_url: str