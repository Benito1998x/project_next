"""
Test de conexión a Tavily API
Solo hace una búsqueda simple para verificar que funciona
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "backend"))


async def test_tavily_connection():
    """Probar conexión a Tavily con una búsqueda simple"""
    print("🧪 TEST DE CONEXIÓN A TAVILY API")
    print("=" * 50)

    # 1. Verificar API key
    tavily_key = os.getenv("TAVILY_API_KEY")

    if not tavily_key:
        print("❌ ERROR: Variable TAVILY_API_KEY no encontrada")
        print("   Asegúrate de tener el archivo .env configurado")
        return False

    print(f"✓ API Key encontrada: {tavily_key[:15]}...")

    # 2. Intentar búsqueda
    try:
        import httpx

        print("\n🔍 Haciendo búsqueda de prueba...")
        print("   Query: 'mercado café Bolivia 2024'")

        response = httpx.post(
            "https://api.tavily.com/search",
            json={
                "api_key": tavily_key,
                "query": "mercado café Bolivia 2024",
                "search_depth": "basic",
                "include_answer": True,
                "max_results": 3,
            },
            timeout=30.0,
        )

        if response.status_code == 200:
            data = response.json()

            print("\n✅ CONEXIÓN EXITOSA")
            print(f"   Status: {response.status_code}")
            print(f"   Resultados encontrados: {len(data.get('results', []))}")

            if data.get("answer"):
                print(f"\n📝 Respuesta resumida:")
                print(f"   {data['answer'][:150]}...")

            print("\n🔗 URLs encontradas:")
            for i, result in enumerate(data.get("results", [])[:3], 1):
                print(f"   {i}. {result.get('title', 'Sin título')}")
                print(f"      {result.get('url', 'Sin URL')[:60]}...")

            print("\n📝 Próximo paso: Integrar en el Agente Investigador")
            return True
        else:
            print(f"\n❌ Error en API: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return False

    except ImportError:
        print("❌ Error: httpx no instalado")
        print("   Ejecuta: pip install httpx")
        return False
    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")
        return False


def main():
    """Ejecutar test async"""
    try:
        result = asyncio.run(test_tavily_connection())
        sys.exit(0 if result else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrumpido")
        sys.exit(1)


if __name__ == "__main__":
    main()
