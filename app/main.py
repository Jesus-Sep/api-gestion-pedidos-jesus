from fastapi import FastAPI

app = FastAPI(title="API Gestión de Pedidos")

@app.get("/")
def root():
    return {"message": "API de Gestión de Pedidos activa"}
