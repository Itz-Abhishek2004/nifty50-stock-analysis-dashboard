import pandas as pd
import plotly.express as px
import streamlit as st

# ---------- Page config ----------
st.set_page_config(
    page_title="Nifty 50 Stock Dashboard",
    layout="wide",
)

# ---------- Data loading ----------
@st.cache_data
def load_data():
    daily = pd.read_csv("data_processed/all_stocks_daily.csv", parse_dates=["date"])
    yearly = pd.read_csv("data_processed/yearly_return_with_sector.csv")
    vol = pd.read_csv("data_processed/volatility_per_ticker.csv")
    sector_perf = pd.read_csv("data_processed/sector_performance.csv")
    monthly_g = pd.read_csv("data_processed/top5_gainers_per_month.csv")
    monthly_l = pd.read_csv("data_processed/top5_losers_per_month.csv")
    return daily, yearly, vol, sector_perf, monthly_g, monthly_l

daily, yearly, vol, sector_perf, monthly_g, monthly_l = load_data()

# Basic cleaning
daily["ticker"] = daily["ticker"].str.strip()
yearly["ticker"] = yearly["ticker"].str.strip()
vol["ticker"] = vol["ticker"].str.strip()

# ---------- Sidebar filters ----------
tickers = sorted(daily["ticker"].unique())
default_tickers = tickers[:5] if len(tickers) >= 5 else tickers

st.sidebar.title("Controls")

selected_tickers = st.sidebar.multiselect(
    "Select tickers for price & returns",
    options=tickers,
    default=default_tickers,
)

st.sidebar.markdown("---")
st.sidebar.markdown("Data source: Nifty 50 daily OHLCV (YAML → CSV)")

# ---------- Main layout: Tabs ----------
st.title("Nifty 50 Stock Performance Dashboard")

main_tab, risk_tab, sector_tab, monthly_tab = st.tabs(
    ["Market Overview", "Volatility & Returns", "Sector Performance", "Monthly Movers"]
)

# ---------- Tab 1: Market Overview ----------
with main_tab:
    st.header("Market Overview")

    # Market summary metrics
    green = (yearly["yearly_return"] > 0).sum()
    red = (yearly["yearly_return"] <= 0).sum()
    total = len(yearly)

    avg_close = daily["close"].mean()
    avg_volume = daily["volume"].mean()

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Stocks", total)
    c2.metric("Green Stocks", green)
    c3.metric("Red Stocks", red)
    c4.metric("Avg Close Price", f"{avg_close:.2f}")
    c5.metric("Avg Volume", f"{avg_volume:,.0f}")

    st.markdown("### Top 10 Gainers and Losers (Yearly Return)")

    top_10_green = yearly.sort_values("yearly_return", ascending=False).head(10)
    top_10_red = yearly.sort_values("yearly_return").head(10)

    col_g, col_l = st.columns(2)

    with col_g:
        fig_g = px.bar(
            top_10_green,
            x="ticker",
            y="yearly_return",
            title="Top 10 Gainers",
            labels={"yearly_return": "Yearly Return"},
        )
        fig_g.update_layout(xaxis_title="", yaxis_tickformat=".0%")
        st.plotly_chart(fig_g, use_container_width=True)

    with col_l:
        fig_l = px.bar(
            top_10_red,
            x="ticker",
            y="yearly_return",
            title="Top 10 Losers",
            labels={"yearly_return": "Yearly Return"},
        )
        fig_l.update_layout(xaxis_title="", yaxis_tickformat=".0%")
        st.plotly_chart(fig_l, use_container_width=True)

# ---------- Tab 2: Volatility & Returns ----------
with risk_tab:
    st.header("Volatility & Time-Series Returns")

    # Volatility chart
    st.subheader("Top 10 Most Volatile Stocks")

    top_10_vol = vol.sort_values("volatility", ascending=False).head(10)
    fig_vol = px.bar(
        top_10_vol,
        x="ticker",
        y="volatility",
        title="Top 10 Most Volatile Stocks (Std Dev of Daily Returns)",
        labels={"volatility": "Volatility"},
    )
    fig_vol.update_layout(xaxis_title="", yaxis_tickformat=".2%")
    st.plotly_chart(fig_vol, use_container_width=True)

    st.subheader("Price & Cumulative Return (Selected Tickers)")

    if selected_tickers:
        sub = daily[daily["ticker"].isin(selected_tickers)].copy()
        sub = sub.sort_values(["ticker", "date"])
        sub["daily_return"] = sub.groupby("ticker")["close"].pct_change()
        sub["cumulative_return"] = (
            (1 + sub["daily_return"]).groupby(sub["ticker"]).cumprod() - 1
        )

        t1, t2 = st.tabs(["Price", "Cumulative Return"])

        with t1:
            fig_price = px.line(
                sub,
                x="date",
                y="close",
                color="ticker",
                title="Daily Close Price",
            )
            fig_price.update_layout(xaxis_title="", yaxis_title="Close Price")
            st.plotly_chart(fig_price, use_container_width=True)

        with t2:
            fig_cum = px.line(
                sub,
                x="date",
                y="cumulative_return",
                color="ticker",
                title="Cumulative Return (from start of dataset)",
            )
            fig_cum.update_layout(
                xaxis_title="", yaxis_title="Cumulative Return", yaxis_tickformat=".0%"
            )
            st.plotly_chart(fig_cum, use_container_width=True)
    else:
        st.info("Select at least one ticker from the sidebar to see time-series charts.")

# ---------- Tab 3: Sector Performance ----------
with sector_tab:
    st.header("Sector-wise Performance")

    fig_sector = px.bar(
        sector_perf,
        x="sector",
        y="yearly_return",
        title="Average Yearly Return by Sector",
        labels={"yearly_return": "Avg Yearly Return"},
    )
    fig_sector.update_layout(xaxis_title="", yaxis_tickformat=".1%")
    st.plotly_chart(fig_sector, use_container_width=True)

    st.subheader("Yearly Returns with Sector Detail")
    st.dataframe(
        yearly[["ticker", "yearly_return", "sector"]]
        .sort_values("yearly_return", ascending=False)
        .reset_index(drop=True)
    )

# ---------- Tab 4: Monthly Movers ----------
with monthly_tab:
    st.header("Monthly Top 5 Gainers and Losers")

    months = sorted(monthly_g["month"].unique())
    if months:
        selected_month = st.selectbox("Select Month", options=months, index=0)

        mg = monthly_g[monthly_g["month"] == selected_month]
        ml = monthly_l[monthly_l["month"] == selected_month]

        col_mg, col_ml = st.columns(2)

        with col_mg:
            fig_mg = px.bar(
                mg,
                x="ticker",
                y="monthly_return",
                title=f"Top 5 Gainers - {selected_month}",
                labels={"monthly_return": "Monthly Return"},
            )
            fig_mg.update_layout(xaxis_title="", yaxis_tickformat=".0%")
            st.plotly_chart(fig_mg, use_container_width=True)

        with col_ml:
            fig_ml = px.bar(
                ml,
                x="ticker",
                y="monthly_return",
                title=f"Top 5 Losers - {selected_month}",
                labels={"monthly_return": "Monthly Return"},
            )
            fig_ml.update_layout(xaxis_title="", yaxis_tickformat=".0%")
            st.plotly_chart(fig_ml, use_container_width=True)
    else:
        st.info("No monthly data available.")
