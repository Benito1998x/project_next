"""
Cliente para OpenCode Go API.
Solo para uso en desarrollo/testing (alternativa gratuita a MiniMax).
"""

import httpx
from core.config import settings
from core.exceptions import ExternalAPIError


class OpenCodeGoClient:
    """
    Cliente para API de OpenCode Go.
    Uso: Desarrollo y testing (no requiere API key de pago).
    Documentación: https://opencode.ai/docs
    """

    BASE_URL = "https://api.opencode.ai/v1"

    def __init__(self, api_key: str = None):
        # Usar OPENCODE_API_KEY si existe, sino None (algunas instancias locales no requieren key)
        self.api_key = api_key or getattr(settings, "opencode_api_key", None)
        self.headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            self.headers["Authorization"] = f"Bearer {self.api_key}"

    async def generate_text(
        self,
        prompt: str,
        system_prompt: str = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> str:
        """
        Generar texto usando OpenCode Go.

        Args:
            prompt: Prompt del usuario
            system_prompt: Instrucciones del sistema (opcional)
            temperature: Creatividad (0.0 - 1.0)
            max_tokens: Límite de tokens

        Returns:
            Texto generado
        """
        url = f"{self.BASE_URL}/chat/completions"

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": "opencode-go",
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
            raise ExternalAPIError("OpenCodeGo", f"HTTP error: {str(e)}", e)
        except (KeyError, IndexError) as e:
            raise ExternalAPIError(
                "OpenCodeGo", f"Invalid response format: {str(e)}", e
            )
        except Exception as e:
            raise ExternalAPIError("OpenCodeGo", f"Unexpected error: {str(e)}", e)


class LLMClientFactory:
    """
    Factory para seleccionar el cliente LLM según el entorno.

    Desarrollo: OpenCode Go (gratuito)
    Producción: MiniMax 2.5 (pago, mejor calidad)
    """

    @staticmethod
    def get_client(env: str = None):
        """
        Obtener cliente LLM según entorno.

        Args:
            env: 'development' o 'production'. Si es None, usa settings.APP_ENV
        """
        from core.config import settings

        environment = env or settings.app_env

        if environment == "production":
            from .minimax_client import MiniMaxClient

            return MiniMaxClient()
        else:
            return OpenCodeGoClient()
