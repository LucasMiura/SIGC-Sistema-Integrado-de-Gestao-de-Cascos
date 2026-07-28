from fastapi import FastAPI

from src.api.routes import (
    purchase_tracking_router,
    supplier_contact_router,
    supplier_router,
)


app = FastAPI(
    title="SIGC",
    description="Sistema Integrado de Gestão de Cascos",
    version="0.1.0",
)


app.include_router(purchase_tracking_router)
app.include_router(supplier_router)
app.include_router(supplier_contact_router)


@app.get(
    "/",
    tags=["Sistema"],
    summary="Verificar funcionamento do sistema",
)
def root() -> dict[str, str]:
    """Retorna informações básicas sobre a aplicação."""

    return {
        "sistema": "SIGC",
        "mensagem": (
            "Sistema Integrado de Gestão de Cascos "
            "em funcionamento."
        ),
        "versao": "0.1.0",
    }