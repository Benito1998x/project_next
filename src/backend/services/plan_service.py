"""
Servicio de lógica de negocio para planes.
Orquesta entre repositorios y servicios externos.
"""

from typing import Optional, List
from repositories.base import PlanRepository
from models.plan import Plan, PlanCreate


class PlanService:
    """
    Servicio que encapsula la lógica de negocio de planes.
    """

    def __init__(self, repository: PlanRepository):
        self.repository = repository

    async def create_plan(self, plan_data: PlanCreate) -> Plan:
        """Crear un nuevo plan de negocio"""
        # Aquí iría lógica adicional: validaciones, triggers, etc.
        return await self.repository.create(plan_data)

    async def get_plan(self, plan_id: str) -> Optional[Plan]:
        """Obtener un plan por ID"""
        return await self.repository.get_by_id(plan_id)

    async def list_plans(self, limit: int = 100, offset: int = 0) -> List[Plan]:
        """Listar planes con paginación"""
        return await self.repository.list_all(limit, offset)

    async def update_plan(self, plan_id: str, plan_data: dict) -> Optional[Plan]:
        """Actualizar un plan"""
        return await self.repository.update(plan_id, plan_data)

    async def delete_plan(self, plan_id: str) -> bool:
        """Eliminar un plan"""
        return await self.repository.delete(plan_id)
