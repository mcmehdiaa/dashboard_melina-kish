
import streamlit as st
import pandas as pd
import plotly.express as px

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

# 📊 نمودار میله‌ای پیشرفت به تفکیک پیمانکار
st.subheader("📊 نمودار میله‌ای پیشرفت واقعی به تفکیک پیمانکار")
contractor_progress = (
    filtered_df.groupby("Contractor")[["Actual Progress I", "Planned Progress I"]]
    .mean()
    .reset_index()
    .melt(id_vars="Contractor", var_name="نوع پیشرفت", value_name="درصد")
)
fig_bar = px.bar(contractor_progress, x="Contractor", y="درصد", color="نوع پیشرفت",
                 barmode="group", text_auto=True,
                 color_discrete_map={"Planned Progress I": "#1f77b4", "Actual Progress I": "#ff7f0e"})
fig_bar.update_layout(title="مقایسه میانگین پیشرفت واقعی و برنامه‌ای پیمانکاران")
st.plotly_chart(fig_bar, use_container_width=True)

# 📊 نمودار میله‌ای روند تجمعی پیشرفت
st.subheader("📊 نمودار میله‌ای روند تجمعی پیشرفت")
filtered_df["Start"] = filtered_df["Start"].astype(str)
filtered_df = filtered_df[filtered_df["Start"].str.contains("/")]
filtered_df["Start_Date"] = pd.to_datetime(filtered_df["Start"], format="%Y/%m/%d", errors="coerce")
timeline_df = filtered_df.sort_values("Start_Date").copy()
timeline_df["Cumulative Planned"] = timeline_df["Planned Progress I"].cumsum()
timeline_df["Cumulative Actual"] = timeline_df["Actual Progress I"].cumsum()
timeline_bar = timeline_df[["Start_Date", "Cumulative Planned", "Cumulative Actual"]].copy()
timeline_bar = timeline_bar.melt(id_vars="Start_Date", var_name="نوع پیشرفت", value_name="ارزش تجمعی")
fig_trend_bar = px.bar(timeline_bar, x="Start_Date", y="ارزش تجمعی", color="نوع پیشرفت",
                       barmode="group",
                       color_discrete_map={"Cumulative Planned": "#1f77b4", "Cumulative Actual": "#ff7f0e"})
fig_trend_bar.update_layout(title="نمودار میله‌ای تجمعی پیشرفت")
st.plotly_chart(fig_trend_bar, use_container_width=True)

# 📉 نمودار S Curve (PV / EV / AC)
st.subheader("📉 نمودار S Curve (EV / PV / AC)")
timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()
timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()
timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()
fig_s_curve = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"],
                      labels={"value": "ارزش تجمعی", "Start_Date": "تاریخ"},
                      color_discrete_map={
                          "PV": "#1f77b4",
                          "EV": "#ff7f0e",
                          "AC": "#7f7f7f"
                      })
fig_s_curve.update_layout(title="نمودار S Curve (PV / EV / AC)")
st.plotly_chart(fig_s_curve, use_container_width=True)

# جدول نهایی
st.subheader("📋 جدول نهایی فعالیت‌ها")
st.dataframe(filtered_df, use_container_width=True)
