from fastapi import FastAPI
from api.routes.ifpimon_routes import router as ifpimon_routes
from api.routes.root_routes import router as ifpimon_root_router
from api.exceptions.handlers import register_exception_handlers

# Iniciamos o APP utilizando o handler
app = FastAPI()
register_exception_handlers(app)

# Rota raiz
app.include_router(
    ifpimon_root_router
)

# Rotas da API
app.include_router(
    ifpimon_routes,
    prefix="/api"
)