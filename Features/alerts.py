import streamlit as st

def render_alerts(df):

    critical = df[df["risk_level"] == "Crítico"]

    if not critical.empty:

        st.error(
            "Risco crítico detectado!"
        )

        if st.button(
            "Aprovar envio de alerta"
        ):

            st.session_state.alerts_sent += 1

            st.success(
                "Alerta enviado."
            )