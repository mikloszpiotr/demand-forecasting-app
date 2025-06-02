import pandas as pd

def load_and_prepare_data(csv_file):
    df = pd.read_csv(csv_file, parse_dates=["date"])
    df = df.sort_values("date")
    df = df.set_index("date")
    df = df.resample("D").sum()  # daily resampling
    df["quantity"].fillna(method="ffill", inplace=True)  # forward fill missing
    return df
