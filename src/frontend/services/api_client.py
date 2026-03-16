"""
Cliente HTTP para comunicarse con el backend FastAPI.
"""

import requests
from typing import Optional, Dict, Any


class APIClient:
    """Cliente para API del backend"""

    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.api_v1 = f"{base_url}/api/v1"

    def health_check(self) -> Dict[str, Any]:
        """Verificar estado del backend"""
        try:
            response = requests.get(f"{self.api_v1}/health", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}

    def create_plan(self, plan_data: dict) -> Dict[str, Any]:
        """Crear un nuevo plan"""
        try:
            response = requests.post(
                f"{self.api_v1}/planes", json=plan_data, timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_plan(self, plan_id: str) -> Dict[str, Any]:
        """Obtener un plan por ID"""
        try:
            response = requests.get(f"{self.api_v1}/planes/{plan_id}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def list_plans(self) -> Dict[str, Any]:
        """Listar todos los planes"""
        try:
            response = requests.get(f"{self.api_v1}/planes", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}


# Instancia global
api_client = APIClient()
