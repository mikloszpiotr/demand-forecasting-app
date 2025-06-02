# Demand Forecasting App

This app forecasts future product demand using historical data. It is built with Streamlit, Python, and common ML libraries.

## Features
- Upload CSV data
- View historical demand
- Forecast future demand (moving average baseline)
- Visualize results interactively

## Project Structure
- `app.py` – main Streamlit app
- `data/` – raw data
- `utils/` – data processing, forecasting, and plotting functions
- `models/` – saved models (if needed)

## Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```
