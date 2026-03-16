"""
Vista Home - Página principal de BPAE.
"""

import streamlit as st
from services.api_client import api_client


def render_home():
    """Renderizar página de inicio"""

    st.title("🏢 Business Plan Automation Engine")
    st.subtitle("Genera planes de negocio profesionales con IA")

    # Verificar conexión con backend
    with st.spinner("Verificando conexión..."):
        health = api_client.health_check()

    if health.get("status") == "ok":
        st.success("✅ Backend conectado correctamente")
    else:
        st.error("❌ No se puede conectar al backend")
        st.info(
            "Asegúrate de que el servidor FastAPI esté corriendo en http://localhost:8000"
        )

    st.divider()

    # Descripción
    st.markdown("""
    ### ¿Qué puedes hacer?
    
    1. **Crear Plan** - Inicia un nuevo plan de negocio
    2. **Ver Planes** - Consulta planes existentes
    3. **Generar Secciones** - Usa IA para generar análisis
    4. **Descargar** - Obtén el documento final en Word/Excel
    
    ### Stack Tecnológico
    - **Backend**: FastAPI + Supabase
    - **Frontend**: Streamlit
    - **IA**: MiniMax 2.5
    - **Investigación**: Tavily API
    """)

    # Botón para empezar
    if st.button("➕ Crear Nuevo Plan", type="primary", use_container_width=True):
        st.switch_page("views/create_plan.py")
