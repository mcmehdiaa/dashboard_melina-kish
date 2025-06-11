
import streamlit as st
import pandas as pd
import plotly.express as px

# بارگذاری داده‌ها
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTASI7kKjouIBQffl3Cpkm5nKs9L8ionS1nFaJRXY-nJ5rjDpHVx-vjLxFTNtYAeQ/pub?output=csv"
df = pd.read_csv(csv_url)

st.set_page_config(page_title="S Curve پروژه ملینا کیش", layout="wide")
st.title("📈 نمودار S Curve - پروژه ملینا کیش")

# آماده‌سازی داده‌ها
df["Start"] = df["Start"].astype(str)
df = df[df["Start"].str.contains("/")]
df["Start_Date"] = pd.to_datetime(df["Start"], format="%Y/%m/%d", errors="coerce")

df = df.sort_values("Start_Date").copy()
df["PV"] = df["Planned Progress I"].cumsum()
df["EV"] = df["Actual Progress I"].cumsum()
df["AC"] = df["Actual Cost"].fillna(0).cumsum()

# رسم نمودار S Curve
fig_s_curve = px.line(df, x="Start_Date", y=["PV", "EV", "AC"],
                      labels={"value": "ارزش تجمعی", "Start_Date": "تاریخ"},
                      color_discrete_map={
                          "PV": "#1f77b4",  # آبی
                          "EV": "#ff7f0e",  # نارنجی
                          "AC": "#7f7f7f"   # خاکستری
                      })

fig_s_curve.update_layout(title="📊 نمودار S Curve (PV / EV / AC)",
                          legend_title_text="شاخص‌ها")

st.plotly_chart(fig_s_curve, use_container_width=True)

# جدول داده‌ها
st.subheader("📋 جدول داده‌های S Curve")
st.dataframe(df[["Start_Date", "PV", "EV", "AC"]], use_container_width=True)
