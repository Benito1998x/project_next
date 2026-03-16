"""
Test básico para endpoint /health
"""

import pytest
from httpx import AsyncClient
import sys
import os

# Añadir src/backend al path
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src", "backend")
)

from main import app


@pytest.mark.asyncio
async def test_health_check():
    """Test que el endpoint /health responde correctamente"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "service" in response.json()
