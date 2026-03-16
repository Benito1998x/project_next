"""
Entry point de la aplicación FastAPI.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from api.v1 import health, planes


def create_application() -> FastAPI:
    """Factory function para crear la aplicación FastAPI"""

    app = FastAPI(
        title=settings.app_name,
        description="Business Plan Automation Engine API",
        version="0.1.0",
        debug=settings.debug,
    )

    # Configurar CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Registrar routers
    app.include_router(health.router, prefix=settings.api_v1_prefix)
    app.include_router(planes.router, prefix=settings.api_v1_prefix)

    return app


# Instancia de la aplicación
app = create_application()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.debug)
