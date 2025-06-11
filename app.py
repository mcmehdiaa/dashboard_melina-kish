
import streamlit as st
import pandas as pd
import plotly.express as px

# بارگذاری داده‌ها از Google Sheets منتشر شده به صورت CSV
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTASI7kKjouIBQffl3Cpkm5nKs9L8ionS1nFaJRXY-nJ5rjDpHVx-vjLxFTNtYAeQ/pub?output=csv"
df = pd.read_csv(csv_url)

st.set_page_config(page_title="داشبورد پروژه ملینا کیش", layout="wide")
st.title("📊 داشبورد پروژه ملینا کیش")

# فیلتر بر اساس پیمانکار، طبقه و موقعیت
contractors = st.multiselect("پیمانکار:", options=df["Contractor"].dropna().unique())
floors = st.multiselect("طبقه:", options=df["Floors"].dropna().unique())
positions = st.multiselect("موقعیت:", options=df["Position"].dropna().unique())

filtered_df = df.copy()
if contractors:
    filtered_df = filtered_df[filtered_df["Contractor"].isin(contractors)]
if floors:
    filtered_df = filtered_df[filtered_df["Floors"].isin(floors)]
if positions:
    filtered_df = filtered_df[filtered_df["Position"].isin(positions)]

# شاخص‌های کلی پروژه
st.subheader("📈 شاخص‌های کلی پروژه")
col1, col2 = st.columns(2)
with col1:
    st.metric("میانگین SPI", round(filtered_df["SPI_Calc"].mean(), 2))
with col2:
    st.metric("میانگین CPI", round(filtered_df["CPI_Calc"].mean(), 2))

# نمودار میله‌ای پیشرفت به تفکیک پیمانکار
st.subheader("📊 نمودار پیشرفت واقعی و برنامه‌ای به تفکیک پیمانکار")
contractor_progress = (
    filtered_df.groupby("Contractor")[["Actual Progress I", "Planned Progress I"]]
    .mean()
    .reset_index()
    .melt(id_vars="Contractor", var_name="نوع پیشرفت", value_name="درصد")
)
fig1 = px.bar(contractor_progress, x="Contractor", y="درصد", color="نوع پیشرفت",
              barmode="group", text_auto=True,
              color_discrete_map={"Planned Progress I": "#1f77b4", "Actual Progress I": "#ff7f0e"})
st.plotly_chart(fig1, use_container_width=True)

# اصلاح تاریخ و آماده‌سازی داده برای روند تجمعی و S Curve
filtered_df["Start"] = filtered_df["Start"].astype(str)
filtered_df = filtered_df[filtered_df["Start"].str.contains("/")]
filtered_df["Start_Date"] = pd.to_datetime(filtered_df["Start"], format="%Y/%m/%d", errors="coerce")
timeline_df = filtered_df.sort_values("Start_Date").copy()

# نمودار میله‌ای روند تجمعی پیشرفت
st.subheader("📊 نمودار میله‌ای تجمعی پیشرفت پروژه")
timeline_df["Cumulative Planned"] = timeline_df["Planned Progress I"].cumsum()
timeline_df["Cumulative Actual"] = timeline_df["Actual Progress I"].cumsum()
melted = timeline_df[["Start_Date", "Cumulative Planned", "Cumulative Actual"]].melt(id_vars="Start_Date", var_name="نوع", value_name="درصد")
fig2 = px.bar(melted, x="Start_Date", y="درصد", color="نوع", barmode="group",
              color_discrete_map={"Cumulative Planned": "#1f77b4", "Cumulative Actual": "#ff7f0e"})
st.plotly_chart(fig2, use_container_width=True)

# نمودار S Curve با PV / EV / AC
st.subheader("📉 نمودار S Curve (EV / PV / AC)")
timeline_df["PV"] = timeline_df["Planned Progress I"].cumsum()
timeline_df["EV"] = timeline_df["Actual Progress I"].cumsum()
timeline_df["AC"] = timeline_df["AC"].fillna(0).cumsum()
fig3 = px.line(timeline_df, x="Start_Date", y=["PV", "EV", "AC"],
               labels={"value": "ارزش تجمعی", "Start_Date": "تاریخ"},
               color_discrete_map={"PV": "#1f77b4", "EV": "#ff7f0e", "AC": "#7f7f7f"})
fig3.update_layout(title="S Curve - EV / PV / AC")
st.plotly_chart(fig3, use_container_width=True)

# جدول داده‌های نهایی
st.subheader("📋 جدول اطلاعات فیلترشده")
st.dataframe(filtered_df, use_container_width=True)
