from fastapi import APIRouter
from app.controladores.estado_controlador import health_check

router = APIRouter()

@router.get("/health", status_code=200)
def check_health():
    return health_check()
#endpoint get 
