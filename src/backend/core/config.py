"""
Configuración centralizada del backend BPAE.
Usa Pydantic Settings para cargar variables de entorno.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    """Configuración de la aplicación cargada desde .env"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignorar variables extras en .env
    )

    # App
    app_name: str = Field(default="BPAE API", description="Nombre de la aplicación")
    app_env: str = Field(
        default="development", description="Entorno: development/production"
    )
    debug: bool = Field(default=True, description="Modo debug")

    # APIs Externas
    minimax_api_key: str = Field(default="", description="MiniMax API Key (producción)")
    tavily_api_key: str = Field(..., description="Tavily API Key (requerido)")
    opencode_api_key: str = Field(
        default="", description="OpenCode Go API Key (desarrollo, opcional)"
    )

    # Database
    supabase_url: str = Field(..., description="Supabase Project URL (requerido)")
    supabase_key: str = Field(..., description="Supabase Service Role Key (requerido)")

    # API
    api_v1_prefix: str = "/api/v1"
    allowed_origins: list[str] = Field(
        default=["*"], description="CORS allowed origins"
    )


# Instancia global de settings
settings = Settings()
