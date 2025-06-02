import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from statsmodels.tsa.arima.model import ARIMA
import xgboost as xgb
import numpy as np

def moving_average_forecast(df, horizon):
    forecast = df["quantity"].rolling(window=7).mean().iloc[-1]
    future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=horizon)
    forecast_df = pd.DataFrame({"quantity": [forecast] * horizon}, index=future_dates)
    return forecast_df

def arima_forecast(df, horizon):
    model = ARIMA(df["quantity"], order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=horizon)
    future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=horizon)
    forecast_df = pd.DataFrame({"quantity": forecast}, index=future_dates)
    return forecast_df

def xgboost_forecast(df, horizon):
    df = df.copy()
    df["day"] = range(len(df))
    X = df[["day"]]
    y = df["quantity"]

    model = xgb.XGBRegressor(n_estimators=100)
    model.fit(X, y)

    future_days = np.arange(len(df), len(df) + horizon).reshape(-1, 1)
    preds = model.predict(future_days)
    future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=horizon)
    forecast_df = pd.DataFrame({"quantity": preds}, index=future_dates)
    return forecast_df

def calculate_metrics(actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    mape = mean_absolute_percentage_error(actual, predicted)
    return {"MAE": mae, "MAPE": mape}
