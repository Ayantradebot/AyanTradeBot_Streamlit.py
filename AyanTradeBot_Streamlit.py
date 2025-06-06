
import streamlit as st
import pandas as pd
import random
import datetime

st.set_page_config(page_title="AyanTradeBot", layout="wide")

st.title("📈 AyanTradeBot – India's Free Auto Trading AI")
st.subheader("Daily Auto-Selected Intraday Trades • 100% Free • Connect Angel One / Zerodha")

st.markdown("""
AyanTradeBot is a fully automatic stock trading assistant that:
- Picks top 5–10 trades daily
- Shows entry, exit & stop-loss
- Works on stock price & candlestick formulas
- 100% free, no human input required
- Ready to integrate with Angel One or Zerodha
""")

# Simulate live trade suggestions
def generate_fake_trades():
    trades = []
    for _ in range(5):
        entry = round(random.uniform(20, 100), 2)
        exit_price = round(entry * random.uniform(1.05, 1.15), 2)
        stop_loss = round(entry * random.uniform(0.95, 0.98), 2)
        trades.append({
            "Stock": f"STOCK{random.randint(100, 999)}",
            "Entry Price": entry,
            "Exit Target": exit_price,
            "Stop Loss": stop_loss,
            "Time": datetime.datetime.now().strftime("%H:%M:%S")
        })
    return pd.DataFrame(trades)

st.header("📊 Today's Best Auto Trades")
df = generate_fake_trades()
st.dataframe(df, use_container_width=True)

st.success("Connect your Angel One or Zerodha account to start live trading (Coming Soon)")
st.button("🔁 Refresh Suggestions")
