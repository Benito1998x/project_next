"""
Test de conexión a Supabase
Solo verifica que podemos conectar y hacer una consulta simple
"""

import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Agregar src/backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "backend"))


def test_supabase_connection():
    """Probar conexión básica a Supabase"""
    print("🧪 TEST DE CONEXIÓN A SUPABASE")
    print("=" * 50)

    # 1. Verificar variables de entorno
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url or not supabase_key:
        print("❌ ERROR: Variables SUPABASE_URL o SUPABASE_KEY no encontradas")
        print("   Asegúrate de tener el archivo .env configurado")
        return False

    print(f"✓ Variables de entorno encontradas")
    print(f"  URL: {supabase_url[:30]}...")
    print(f"  Key: {supabase_key[:20]}...")

    # 2. Intentar importar y conectar
    try:
        from supabase import create_client

        print("\n✓ Cliente Supabase importado correctamente")

        # Crear cliente
        client = create_client(supabase_url, supabase_key)
        print("✓ Cliente creado")

        # 3. Hacer una consulta simple (listar tablas o health check)
        # Intentamos hacer una consulta a información del servidor
        try:
            # Consulta simple: intentar obtener la versión de PostgREST
            import httpx

            response = httpx.get(
                f"{supabase_url}/rest/v1/", headers={"apikey": supabase_key}
            )

            if response.status_code == 200:
                print("\n✅ CONEXIÓN EXITOSA")
                print(f"   Status: {response.status_code}")
                print(f"   Servidor respondió correctamente")
                print("\n📝 Próximo paso: Crear la tabla 'planes'")
                return True
            else:
                print(f"\n⚠️  Respuesta inesperada: {response.status_code}")
                print(f"   Body: {response.text[:200]}")
                return False

        except Exception as e:
            print(f"\n❌ Error en consulta: {str(e)}")
            return False

    except ImportError as e:
        print(f"❌ Error importando supabase: {str(e)}")
        print("   Ejecuta: pip install supabase")
        return False
    except Exception as e:
        print(f"❌ Error de conexión: {str(e)}")
        return False


if __name__ == "__main__":
    success = test_supabase_connection()
    sys.exit(0 if success else 1)
