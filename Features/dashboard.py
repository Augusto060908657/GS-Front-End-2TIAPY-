import streamlit as st

from UI.cards import metric_card
from UI.charts import risk_plot
from UI.charts import temperature_plot

def render_dashboard(df):

    c1, c2, c3 = st.columns(3)

    with c1:
        metric_card(
            "Temperatura Média",
            f"{df['temperature'].mean():.1f}°C"
        )

    with c2:
        metric_card(
            "Risco Médio",
            f"{df['risk_score'].mean():.1f}"
        )

    with c3:
        metric_card(
            "Anomalias",
            int(df["anomaly"].sum())
        )

    risk_plot(df)

    temperature_plot(df)
