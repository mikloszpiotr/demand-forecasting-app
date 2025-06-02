import matplotlib.pyplot as plt

def plot_forecast(history_df, forecast_df):
    fig, ax = plt.subplots(figsize=(10, 4))
    history_df["quantity"].plot(ax=ax, label="Historical")
    forecast_df["quantity"].plot(ax=ax, label="Forecast", linestyle="--")
    ax.set_title("Demand Forecast")
    ax.set_ylabel("Quantity")
    ax.legend()
    return fig
