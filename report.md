# Project Report: Nifty 50 Stock Performance Analysis

## Problem Statement
The goal of this project is to analyze Nifty 50 stock data and build dashboards that highlight return, volatility, and sector-level insights.

## Dataset Description
The dataset contains daily stock-level information such as date, ticker, close price, and volume. Processed CSV files were created for yearly returns, volatility, sector performance, and monthly gainers/losers.

## Tools Used
- Python for data cleaning and analysis
- SQL for structured data handling
- Streamlit for interactive dashboard development
- Power BI for reporting dashboard creation
- GitHub for version control and project hosting


## Data Processing Steps
1. Loaded stock data.
2. Cleaned missing values and standardized fields.
3. Calculated yearly return for each stock.
4. Calculated monthly return and identified top 5 gainers and losers.
5. Calculated volatility using daily return standard deviation.
6. Aggregated average yearly return by sector.

## Analysis Performed
- Top 10 yearly gainers and losers
- Volatility comparison across stocks
- Sector-wise yearly return analysis
- Monthly top 5 gainers and losers
- Price and cumulative return tracking for selected stocks

## Dashboard Development
A Streamlit dashboard was built using tabs, KPI metrics, and interactive charts. A Power BI dashboard was also created using cards and bar charts for quick business-style reporting.

## Key Findings
- Stock performance differed widely across the Nifty 50 universe.
- Some sectors delivered stronger average returns than others.
- Highly volatile stocks carried greater risk but also stronger movement potential.
- Monthly winners and losers changed significantly over time.

## Challenges Faced
- Organizing multiple processed datasets for dashboard use
- Learning Power BI basics from scratch
- Managing file paths and clean project structure

## Final Outcome
This project successfully combines Python analysis, SQL-based handling, Streamlit dashboard development, and Power BI reporting in a single workflow.