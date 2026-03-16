"""
Entry point de la aplicación Streamlit.
"""

import streamlit as st
from views.home import render_home
from views.create_plan import render_create_plan
from views.view_plan import render_view_plan

# Configuración de la página
st.set_page_config(
    page_title="BPAE - Business Plan Automation Engine",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation
with st.sidebar:
    st.title("🏢 BPAE")
    st.divider()

    page = st.radio(
        "Navegación",
        ["Inicio", "Crear Plan", "Ver Planes"],
        label_visibility="collapsed",
    )

    st.divider()
    st.caption("Business Plan Automation Engine")
    st.caption("v0.1.0 - MVP")

# Renderizar vista seleccionada
if page == "Inicio":
    render_home()
elif page == "Crear Plan":
    render_create_plan()
elif page == "Ver Planes":
    render_view_plan()
