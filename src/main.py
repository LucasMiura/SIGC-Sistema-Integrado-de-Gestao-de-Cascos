from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from src.core.config import (
    get_cors_origins,
)

from src.api.routes import (
    audit_router,
    customer_return_router,
    dashboard_router,
    outbound_router,
    part_router,
    purchase_router,
    purchase_tracking_router,
    auth_router,
    role_router,
    supplier_contact_router,
    supplier_return_router,
    supplier_router,
    transfer_router,
    transfer_return_router,
    user_router,
)


app = FastAPI(
    title="SIGC",
    description=(
        "Sistema Integrado de Gestão de Cascos"
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=[
        "*",
    ],
    allow_headers=[
        "*",
    ],
)

app.include_router(
    audit_router
)

app.include_router(
    auth_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    role_router
)

app.include_router(
    user_router
)

app.include_router(
    supplier_router
)

app.include_router(
    supplier_contact_router
)

app.include_router(
    part_router
)

app.include_router(
    purchase_router
)

app.include_router(
    purchase_tracking_router
)

app.include_router(
    outbound_router
)

app.include_router(
    customer_return_router
)

app.include_router(
    supplier_return_router
)

app.include_router(
    transfer_router
)

app.include_router(
    transfer_return_router
)


@app.get(
    "/",
    tags=["System"],
)
def root() -> dict[str, str]:
    return {
        "sistema": "SIGC",
        "mensagem": (
            "Sistema Integrado de Gestão de "
            "Cascos em funcionamento."
        ),
        "versao": "0.1.0",
    }