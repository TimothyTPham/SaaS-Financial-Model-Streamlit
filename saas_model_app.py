import streamlit as st
import pandas as pd
import numpy as np

# Title and description
st.title("SaaS Financial Model")
st.write("""
This is a simple SaaS financial model simulator. Adjust inputs to project customer growth, revenue, and key SaaS metrics like MRR, LTV, CAC payback period, and ARR.
""")

# Sidebar inputs
starting_customers = st.sidebar.number_input("Starting Customers", value=100)
monthly_new_customers = st.sidebar.number_input("Monthly New Customers", value=20)
monthly_churn_rate = st.sidebar.slider("Monthly Churn Rate (%)", min_value=0.0, max_value=100.0, value=5.0) / 100
arpu = st.sidebar.number_input("ARPU ($)", value=100)
cac = st.sidebar.number_input("CAC ($)", value=400)
gross_margin = st.sidebar.slider("Gross Margin (%)", min_value=0.0, max_value=100.0, value=80.0) / 100
months = st.sidebar.slider("Time Horizon (Months)", min_value=1, max_value=60, value=12)

# Initialize model
current_customers = starting_customers
data = []

for month in range(1, months + 1):
    churned_customers = current_customers * monthly_churn_rate
    end_customers = current_customers - churned_customers + monthly_new_customers

    rounded_end_customers = round(end_customers)
    mrr = rounded_end_customers * arpu
    arr = mrr * 12
    gross_profit = arr * gross_margin
    customer_acquisition_cost = monthly_new_customers * cac
    ltv = (arpu * gross_margin) / monthly_churn_rate if monthly_churn_rate != 0 else np.nan
    cac_payback_period_months = cac / (arpu * gross_margin) if arpu * gross_margin != 0 else np.nan

    data.append({
        "Month": month,
        "Starting Customers": current_customers,
        "Churned Customers": churned_customers,
        "New Customers": monthly_new_customers,
        "Ending Customers": end_customers,
        "MRR ($)": mrr,
        "ARR ($)": arr,
        "Gross Profit ($)": gross_profit,
        "Customer Acquisition Cost ($)": customer_acquisition_cost,
        "LTV ($)": ltv,
        "CAC Payback Period (Months)": cac_payback_period_months
    })

    current_customers = rounded_end_customers

# Display results
df = pd.DataFrame(data)
st.dataframe(df.style.format({
    "Starting Customers": "{:,.0f}",
    "Churned Customers": "{:,.0f}",
    "New Customers": "{:,.0f}",
    "Ending Customers": "{:,.0f}",
    "MRR ($)": "${:,.2f}",
    "ARR ($)": "${:,.2f}",
    "Gross Profit ($)": "${:,.2f}",
    "Customer Acquisition Cost ($)": "${:,.2f}",
    "LTV ($)": "${:,.2f}",
    "CAC Payback Period (Months)": "{:.1f}"
}))

# Line chart for MRR over time
st.line_chart(df.set_index("Month")["MRR ($)"])

# Optional: Export
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "saas_model.csv", "text/csv")
