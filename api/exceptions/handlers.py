from http import HTTPStatus
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.exceptions.ifpimon_exceptions import IFPIMonNotFoundError


async def ifpimon_not_found_handler(
    request: Request,
    error: IFPIMonNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={
            "error": "ifpimon_not_found",
            "message": (
                f"IFPI Mon com ID {error.ifpimon_id} "
                "não foi encontrado."
            ),
        },
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        IFPIMonNotFoundError,
        ifpimon_not_found_handler,
    )
