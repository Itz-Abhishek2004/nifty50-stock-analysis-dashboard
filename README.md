# Nifty 50 Stock Performance Analysis Dashboard

## Overview
This project analyzes Nifty 50 stock market data using Python, SQL, Streamlit, and Power BI. It focuses on stock returns, volatility, sector-wise performance, and dashboard-based visualization.

## Objectives
- Analyze yearly and monthly stock performance.
- Identify top gainers, top losers, and most volatile stocks.
- Compare sector-wise average returns.
- Build an interactive dashboard in Streamlit.
- Create a Power BI dashboard for reporting.

## Tech Stack
- Python
- Pandas
- NumPy
- SQL / MySQL
- Streamlit
- Plotly
- Power BI
- Git and GitHub

## Project Workflow
1. Collected and cleaned stock data.
2. Processed data into analysis-ready CSV files.
3. Calculated yearly returns, monthly returns, and volatility.
4. Built a Streamlit dashboard with filters and tabs.
5. Built a Power BI dashboard with KPI cards and charts.

## Folder Structure

NIFTY_STOCK_ANALYSIS/
├── README.md
├── report.md
├── requirements.txt
├── data_processed/
├── notebooks/
├── src/
│   └── app.py
├── power bi/
│   └── Nifty50_Dashboard.pbix
└── screenshots/

## Run the Streamlit App
```bash
pip install -r requirements.txt
streamlit run src/app.py
```
## Power BI Dashboard
The Power BI file is available inside the `power bi/` folder. It contains KPI cards, top gainers, top losers, and sector-wise performance visuals.

## Key Insights
- Some sectors performed better than others on average yearly return.
- A few stocks contributed disproportionately to gains and losses.
- Volatility varied significantly across stocks.
- Monthly movers changed over time and highlighted short-term leaders and laggards.

