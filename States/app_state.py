import streamlit as st

def initialize_state():

    if "alerts_sent" not in st.session_state:
        st.session_state.alerts_sent = 0

    if "approved_alerts" not in st.session_state:
        st.session_state.approved_alerts = []