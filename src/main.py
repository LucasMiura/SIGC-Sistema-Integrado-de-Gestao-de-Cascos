from fastapi import FastAPI

app = FastAPI(
    title="SIGC",
    description="Sistema Integrado de Gestão de Cascos",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "sistema": "SIGC",
        "mensagem": "Sistema Integrado de Gestão de Cascos em funcionamento.",
        "versao": "0.1.0"
    }