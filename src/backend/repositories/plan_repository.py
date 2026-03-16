"""
Implementación concreta del repositorio usando Supabase.
"""

from typing import Optional, List
from supabase import Client
from repositories.base import PlanRepository
from models.plan import Plan, PlanCreate
from core.config import settings


class SupabasePlanRepository(PlanRepository):
    """Repositorio que usa Supabase como backend"""

    def __init__(self, client: Client):
        self.client = client
        self.table = "planes"

    async def get_by_id(self, plan_id: str) -> Optional[Plan]:
        """Obtener plan por ID"""
        response = (
            await self.client.table(self.table).select("*").eq("id", plan_id).execute()
        )
        if response.data:
            return Plan(**response.data[0])
        return None

    async def create(self, plan: PlanCreate) -> Plan:
        """Crear nuevo plan"""
        response = (
            await self.client.table(self.table).insert(plan.model_dump()).execute()
        )
        return Plan(**response.data[0])

    async def list_all(self, limit: int = 100, offset: int = 0) -> List[Plan]:
        """Listar planes con paginación"""
        response = (
            await self.client.table(self.table)
            .select("*")
            .limit(limit)
            .offset(offset)
            .execute()
        )
        return [Plan(**item) for item in response.data]

    async def update(self, plan_id: str, plan_data: dict) -> Optional[Plan]:
        """Actualizar plan"""
        response = (
            await self.client.table(self.table)
            .update(plan_data)
            .eq("id", plan_id)
            .execute()
        )
        if response.data:
            return Plan(**response.data[0])
        return None

    async def delete(self, plan_id: str) -> bool:
        """Eliminar plan"""
        response = (
            await self.client.table(self.table).delete().eq("id", plan_id).execute()
        )
        return len(response.data) > 0


# Factory para crear instancia
def get_plan_repository(client: Client) -> PlanRepository:
    """Factory function para obtener repositorio"""
    return SupabasePlanRepository(client)
