"""
Cliente para Tavily API.
Realiza búsquedas web para obtener datos de mercado.
"""

import httpx
from core.config import settings
from core.exceptions import ExternalAPIError


class TavilyClient:
    """
    Cliente para API de Tavily.
    Documentación: https://tavily.com
    """

    BASE_URL = "https://api.tavily.com"

    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.tavily_api_key

    async def search(
        self,
        query: str,
        search_depth: str = "basic",
        include_answer: bool = True,
        max_results: int = 5,
    ) -> dict:
        """
        Realizar búsqueda web.

        Args:
            query: Término de búsqueda
            search_depth: 'basic' o 'advanced'
            include_answer: Incluir respuesta resumida
            max_results: Número máximo de resultados

        Returns:
            Dict con resultados de búsqueda
        """
        url = f"{self.BASE_URL}/search"

        payload = {
            "api_key": self.api_key,
            "query": query,
            "search_depth": search_depth,
            "include_answer": include_answer,
            "max_results": max_results,
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()

        except httpx.HTTPError as e:
            raise ExternalAPIError("Tavily", f"HTTP error: {str(e)}", e)
        except Exception as e:
            raise ExternalAPIError("Tavily", f"Unexpected error: {str(e)}", e)
