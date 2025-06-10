
import streamlit as st
import pandas as pd

# بارگذاری داده‌ها از لینک CSV
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

# نمایش جدول اصلی
st.subheader("📋 جدول فعالیت‌ها")
st.dataframe(filtered_df, use_container_width=True)
