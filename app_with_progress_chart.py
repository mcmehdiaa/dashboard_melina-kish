
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# بارگذاری داده‌ها
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTASI7kKjouIBQffl3Cpkm5nKs9L8ionS1nFaJRXY-nJ5rjDpHVx-vjLxFTNtYAeQ/pub?output=csv"
df = pd.read_csv(csv_url)

st.set_page_config(page_title="داشبورد پروژه ملینا کیش", layout="wide")
st.title("📊 داشبورد پروژه ملینا کیش")

# فیلترها
contractors = st.multiselect("پیمانکار:", options=df["Contractor"].dropna().unique(), default=None)
floors = st.multiselect("طبقه:", options=df["Floors"].dropna().unique(), default=None)
positions = st.multiselect("موقعیت:", options=df["Position"].dropna().unique(), default=None)

filtered_df = df.copy()
if contractors:
    filtered_df = filtered_df[filtered_df["Contractor"].isin(contractors)]
if floors:
    filtered_df = filtered_df[filtered_df["Floors"].isin(floors)]
if positions:
    filtered_df = filtered_df[filtered_df["Position"].isin(positions)]

# شاخص‌های کلی
st.subheader("📈 شاخص‌های کلی پروژه")
col1, col2 = st.columns(2)
with col1:
    st.metric("میانگین SPI", round(filtered_df["SPI_Calc"].mean(), 2))
with col2:
    st.metric("میانگین CPI", round(filtered_df["CPI_Calc"].mean(), 2))

# 📈 نمودار پیشرفت واقعی و برنامه‌ای
st.subheader("📉 نمودار پیشرفت واقعی در مقابل برنامه‌ای")

# فقط فعالیت‌هایی با تاریخ معتبر را در نظر بگیریم
filtered_df["Start"] = filtered_df["Start"].astype(str)
progress_df = filtered_df.copy()
progress_df = progress_df[progress_df["Start"].str.contains("/")]
progress_df["Start_Date"] = pd.to_datetime(progress_df["Start"], format="%Y/%m/%d", errors="coerce")

progress_df = progress_df.sort_values("Start_Date")
fig = go.Figure()
fig.add_trace(go.Scatter(x=progress_df["Start_Date"], y=progress_df["Planned Progress I"],
                         mode='lines+markers', name='برنامه‌ای'))
fig.add_trace(go.Scatter(x=progress_df["Start_Date"], y=progress_df["Actual Progress I"],
                         mode='lines+markers', name='واقعی'))

fig.update_layout(title="پیشرفت برنامه‌ای و واقعی بر اساس زمان شروع فعالیت‌ها",
                  xaxis_title="تاریخ شروع", yaxis_title="درصد پیشرفت", template="simple_white")

st.plotly_chart(fig, use_container_width=True)

# جدول اصلی
st.subheader("📋 جدول فعالیت‌ها")
st.dataframe(filtered_df, use_container_width=True)
