"""
Vista Create Plan - Formulario para crear nuevo plan.
"""

import streamlit as st
from services.api_client import api_client


def render_create_plan():
    """Renderizar formulario de creación de plan"""

    st.title("➕ Crear Nuevo Plan de Negocio")

    with st.form("create_plan_form"):
        st.subheader("Información Básica")

        nombre = st.text_input("Nombre del Negocio *", placeholder="Ej: Café Artesanal")

        rubro = st.selectbox(
            "Rubro *",
            options=[
                "Gastronomía",
                "Tecnología",
                "Retail",
                "Servicios",
                "Manufactura",
                "Otro",
            ],
        )

        ciudad = st.text_input("Ciudad *", placeholder="Ej: La Paz, Bolivia")

        inversion = st.number_input(
            "Inversión Inicial Estimada (BOB)", min_value=0, value=50000, step=1000
        )

        st.divider()

        submitted = st.form_submit_button("Crear Plan", type="primary")

        if submitted:
            if not nombre or not rubro or not ciudad:
                st.error("Por favor completa todos los campos obligatorios (*)")
            else:
                plan_data = {
                    "nombre": nombre,
                    "rubro": rubro,
                    "ciudad": ciudad,
                    "inversion_inicial": inversion,
                }

                with st.spinner("Creando plan..."):
                    result = api_client.create_plan(plan_data)

                if "error" in result:
                    st.error(f"Error: {result['error']}")
                else:
                    st.success("¡Plan creado exitosamente!")
                    st.json(result)

    # Botón para volver
    if st.button("◀️ Volver al Inicio"):
        st.switch_page("main.py")
