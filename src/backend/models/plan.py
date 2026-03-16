"""
Modelos Pydantic para validación de datos.
Representan la estructura de los planes de negocio.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class PlanBase(BaseModel):
    """Campos base de un plan de negocio"""

    nombre: str = Field(
        ..., min_length=3, max_length=200, description="Nombre del negocio"
    )
    rubro: str = Field(..., min_length=2, max_length=100, description="Rubro o sector")
    ciudad: str = Field(
        ..., min_length=2, max_length=100, description="Ciudad de operación"
    )
    inversion_inicial: Optional[float] = Field(
        default=0.0, ge=0, description="Inversión inicial estimada"
    )


class PlanCreate(PlanBase):
    """Modelo para crear un nuevo plan"""

    pass


class PlanResponse(PlanBase):
    """Modelo para respuestas de API"""

    id: str = Field(..., description="UUID del plan")
    estado: str = Field(
        default="borrador", description="Estado: borrador, activo, completado"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


class Plan(PlanResponse):
    """Modelo completo con todos los campos"""

    updated_at: Optional[datetime] = None
    contenido: Optional[dict] = Field(
        default=None, description="Contenido generado por secciones"
    )
