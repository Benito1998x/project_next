"""
Cliente para MiniMax 2.5 API.
Maneja la generación de texto para secciones del plan de negocio.
"""

import httpx
from core.config import settings
from core.exceptions import ExternalAPIError


class MiniMaxClient:
    """
    Cliente para API de MiniMax 2.5.
    Documentación: https://api.minimaxi.chat/v1/text/chatcompletion_v2
    """

    BASE_URL = "https://api.minimaxi.chat/v1"

    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.minimax_api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def generate_text(
        self,
        prompt: str,
        system_prompt: str = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str:
        """
        Generar texto usando MiniMax 2.5.

        Args:
            prompt: Prompt del usuario
            system_prompt: Instrucciones del sistema (opcional)
            temperature: Creatividad (0.0 - 1.0)
            max_tokens: Límite de tokens

        Returns:
            Texto generado
        """
        url = f"{self.BASE_URL}/text/chatcompletion_v2"

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": "MiniMax-Text-01",
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(url, headers=self.headers, json=payload)
                response.raise_for_status()
                data = response.json()

                # Extraer texto de la respuesta
                return data["choices"][0]["message"]["content"]

        except httpx.HTTPError as e:
            raise ExternalAPIError("MiniMax", f"HTTP error: {str(e)}", e)
        except (KeyError, IndexError) as e:
            raise ExternalAPIError("MiniMax", f"Invalid response format: {str(e)}", e)
        except Exception as e:
            raise ExternalAPIError("MiniMax", f"Unexpected error: {str(e)}", e)
