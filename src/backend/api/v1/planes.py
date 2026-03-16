"""
Router para endpoints de planes de negocio.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from models.plan import Plan, PlanCreate

router = APIRouter(prefix="/planes", tags=["planes"])


@router.post("", response_model=Plan)
async def create_plan(plan: PlanCreate):
    """
    Crear un nuevo plan de negocio.

    TODO: Implementar con service + repository
    """
    # Placeholder - implementar en siguiente fase
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("/{plan_id}", response_model=Plan)
async def get_plan(plan_id: str):
    """
    Obtener un plan por ID.

    TODO: Implementar con service + repository
    """
    # Placeholder - implementar en siguiente fase
    raise HTTPException(status_code=501, detail="Not implemented yet")


@router.get("", response_model=List[Plan])
async def list_plans(limit: int = 100, offset: int = 0):
    """
    Listar todos los planes.

    TODO: Implementar con service + repository
    """
    # Placeholder - implementar en siguiente fase
    raise HTTPException(status_code=501, detail="Not implemented yet")
