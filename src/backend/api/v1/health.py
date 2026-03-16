"""
Endpoint de health check para verificar que la API está funcionando.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Verificar estado de la API.
    Retorna 200 OK si todo está funcionando.
    """
    return {"status": "ok", "service": "BPAE API", "version": "0.1.0"}
