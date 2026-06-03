import streamlit as st

from providers.mock_provider import generate_mock_data

from pipelines.risk_pipeline import calculate_fire_risk
from pipelines.anomaly_pipeline import detect_anomalies

from state.app_state import initialize_state

from UI.sidebar import render_sidebar

from features.dashboard import render_dashboard
from features.alerts import render_alerts

initialize_state()

st.set_page_config(
    page_title="FireGuard AI",
    layout="wide"
)

st.title(
    "🔥 FireGuard AI"
)

region, days, threshold = render_sidebar()

@st.cache_data
def load_data(days):

    return generate_mock_data(days)

with st.spinner(
    "Carregando dados climáticos..."
):
    df = load_data(days)

df = calculate_fire_risk(df)

df = detect_anomalies(df)

df = df[
    df["risk_score"] >= threshold
]

tab1, tab2 = st.tabs(
    [
        "Dashboard",
        "Alertas"
    ]
)

with tab1:
    render_dashboard(df)

with tab2:
    render_alerts(df)
