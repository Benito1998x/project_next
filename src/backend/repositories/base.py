"""
Interfaz base para repositorios.
Define el contrato que deben implementar los repositorios concretos.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from models.plan import Plan, PlanCreate


class PlanRepository(ABC):
    """
    Interfaz abstracta para operaciones de Plan.
    Permite cambiar la implementación (Supabase, PostgreSQL, SQLite) sin afectar la lógica de negocio.
    """

    @abstractmethod
    async def get_by_id(self, plan_id: str) -> Optional[Plan]:
        """Obtener un plan por su ID"""
        pass

    @abstractmethod
    async def create(self, plan: PlanCreate) -> Plan:
        """Crear un nuevo plan"""
        pass

    @abstractmethod
    async def list_all(self, limit: int = 100, offset: int = 0) -> List[Plan]:
        """Listar todos los planes con paginación"""
        pass

    @abstractmethod
    async def update(self, plan_id: str, plan_data: dict) -> Optional[Plan]:
        """Actualizar un plan existente"""
        pass

    @abstractmethod
    async def delete(self, plan_id: str) -> bool:
        """Eliminar un plan"""
        pass
