# 📦 Demand Forecasting App

This is a fully interactive web app built with **Streamlit** to forecast product demand using historical time series data. It supports multiple forecasting models and displays evaluation metrics to help you analyze performance.

---

## 🚀 Features

✅ Upload CSV demand data  
✅ Visualize historical sales  
✅ Forecast demand using:
- Moving Average
- ARIMA
- XGBoost

✅ Evaluate forecast accuracy using:
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)

✅ Interactive charts with selectable forecast horizon  
✅ Modular Python architecture (clean code, reusable logic)

---

## 📁 Folder Structure

```
demand_forecasting_app/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Required Python libraries
├── README.md               # Project overview
├── data/                   # Sample data file
│   └── demand_data.csv
├── models/                 # Placeholder for future saved models
└── utils/                  # All logic divided by function
    ├── preprocessing.py    # Data cleaning & resampling
    ├── forecasting.py      # Forecast model logic
    └── visualization.py    # Chart drawing logic
```

---

## 🧪 How to Run the App Locally

### ▶️ 1. Clone this repository:
```bash
git clone https://github.com/yourusername/demand-forecasting-app.git
cd demand-forecasting-app
```

### ▶️ 2. Create and activate virtual environment:
```bash
conda create -n forecast_env python=3.10
conda activate forecast_env
```

### ▶️ 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### ▶️ 4. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 🎯 Business Use Case

This app can help supply chain and operations teams:
- Forecast future product demand
- Reduce stockouts or overstocking
- Evaluate forecasting strategies
- Communicate insights with visual tools

---

## 🧠 About the Author

**Piotr Miklosz**  

