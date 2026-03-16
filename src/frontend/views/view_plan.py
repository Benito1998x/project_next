"""
Vista View Plan - Visualizar un plan existente.
"""

import streamlit as st
from services.api_client import api_client


def render_view_plan():
    """Renderizar vista de plan"""

    st.title("📄 Ver Plan de Negocio")

    # Input para ID del plan
    plan_id = st.text_input("ID del Plan", placeholder="550e8400-e29b-41d4-a716...")

    if st.button("Buscar", type="primary"):
        if plan_id:
            with st.spinner("Buscando plan..."):
                result = api_client.get_plan(plan_id)

            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                st.success("Plan encontrado")
                st.json(result)
        else:
            st.warning("Ingresa un ID de plan")

    st.divider()

    # Lista de planes (placeholder)
    st.subheader("Lista de Planes")
    st.info("Aquí se mostrará la lista de planes (pendiente de implementación)")

    # Botón para volver
    if st.button("◀️ Volver al Inicio"):
        st.switch_page("main.py")
