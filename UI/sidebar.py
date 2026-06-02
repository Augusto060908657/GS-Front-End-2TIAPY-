import streamlit as st

def render_sidebar():

    st.sidebar.title("Filtros")

    region = st.sidebar.selectbox(
        "Região",
        [
            "São Paulo",
            "Paraná",
            "Mato Grosso",
            "Goiás"
        ]
    )

    days = st.sidebar.slider(
        "Período",
        7,
        30,
        15
    )

    threshold = st.sidebar.slider(
        "Threshold de risco",
        0,
        100,
        60
    )

    return region, days, threshold