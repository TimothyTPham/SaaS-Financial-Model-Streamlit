# SaaS Financial Model (Streamlit App)

This project is a simple **Streamlit application** that simulates a SaaS (Software-as-a-Service) financial model over a defined time horizon.

The app allows users to input assumptions such as:
- Starting customer count
- Monthly new customers
- Monthly churn rate
- ARPU (Average Revenue Per User)
- CAC (Customer Acquisition Cost)
- Gross margin
- Number of forecast months

Based on these inputs, the model calculates:
- Monthly Recurring Revenue (MRR)
- Revenue and gross profit
- LTV (Customer Lifetime Value)
- CAC payback period
- Customer growth over time

The app includes:
- Interactive sidebar inputs
- Tabular output of all calculated metrics
- MRR line chart visualization
- Option to download the results as a CSV

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/TimothyTPham/SaaS-Financial-Model-Streamlit.git
cd SaaS-Financial-Model-Streamlit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run saas_model_app.py
```

## 📦 Requirements
- streamlit
- pandas
- numpy

You can install these via pip or use the provided `requirements.txt`.

## 📄 File Overview
- `saas_model_app.py` – Main Streamlit application file
- `requirements.txt` – List of Python packages

---

Created by [Tim Pham](https://github.com/TimothyTPham)
