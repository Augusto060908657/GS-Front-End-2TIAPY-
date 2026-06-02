import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st

def risk_plot(df):

    fig = px.line(
        df,
        y="risk_score",
        title="Evolução do Risco"
    )

    st.plotly_chart(fig, use_container_width=True)

def temperature_plot(df):

    fig, ax = plt.subplots()

    ax.plot(df["temperature"])

    st.pyplot(fig)