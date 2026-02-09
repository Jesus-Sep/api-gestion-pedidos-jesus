from fastapi import APIRouter
from app.controladores.orden_controlador import get_orders, create_order

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/", status_code=200)
def list_orders():
    return get_orders()

@router.post("/", status_code=201)
def new_order(order: dict):
    return create_order(order)

#tenemos dos endpoints get, point