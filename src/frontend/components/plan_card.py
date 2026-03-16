"""
Componente PlanCard - Tarjeta para mostrar resumen de plan.
"""

import streamlit as st


def render_plan_card(plan: dict):
    """
    Renderizar tarjeta de plan.

    Args:
        plan: Dict con datos del plan
    """
    with st.container():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader(plan.get("nombre", "Sin nombre"))
            st.caption(f"Rubro: {plan.get('rubro', 'N/A')}")
            st.caption(f"Ciudad: {plan.get('ciudad', 'N/A')}")

        with col2:
            estado = plan.get("estado", "borrador")
            if estado == "borrador":
                st.badge("Borrador", color="orange")
            elif estado == "activo":
                st.badge("Activo", color="green")
            else:
                st.badge(estado.capitalize())

        st.divider()
