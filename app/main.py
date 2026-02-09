from fastapi import FastAPI
from app.rutas.estado_ruta import router as health_router
from app.rutas.orden_ruta import router as orders_router

##python -m venv venv
#venv\Scripts\activate
#uvicorn app.main:app --reload
app = FastAPI(title="API Gestión de Pedidos")

app.include_router(health_router)
app.include_router(orders_router)

@app.get("/")
def root():
    return {"message": "API de Gestión de Pedidos activa"}

#codigo main