import streamlit as st
import pandas as pd
from utils.preprocessing import load_and_prepare_data
from utils.forecasting import (
    moving_average_forecast,
    arima_forecast,
    xgboost_forecast,
    calculate_metrics
)
from utils.visualization import plot_forecast

st.set_page_config(page_title="Demand Forecasting App", layout="wide")
st.title("📦 Demand Forecasting App")

uploaded_file = st.file_uploader("Upload your demand data CSV", type=["csv"])

if uploaded_file:
    df = load_and_prepare_data(uploaded_file)
    st.subheader("📈 Historical Demand")
    st.line_chart(df["quantity"])

    st.subheader("🔮 Forecast")
    model_choice = st.selectbox("Select Forecasting Model", ["Moving Average", "ARIMA", "XGBoost"])
    horizon = st.slider("Forecast Horizon (days)", 1, 30, 7)

    if model_choice == "Moving Average":
        forecast_df = moving_average_forecast(df, horizon)
    elif model_choice == "ARIMA":
        forecast_df = arima_forecast(df, horizon)
    elif model_choice == "XGBoost":
        forecast_df = xgboost_forecast(df, horizon)

    st.line_chart(forecast_df)

    st.subheader("📊 Forecast Visualization")
    st.pyplot(plot_forecast(df, forecast_df))

    st.subheader("📏 Evaluation Metrics (Last {} Days)".format(horizon))
    if len(df) >= horizon:
        actual = df["quantity"][-horizon:]
        baseline_forecast = moving_average_forecast(df[:-horizon], horizon)["quantity"]
        metrics = calculate_metrics(actual, baseline_forecast)
        st.write("Using Moving Average as baseline:")
        st.write(metrics)
    else:
        st.warning("Not enough historical data to evaluate forecast accuracy.")
