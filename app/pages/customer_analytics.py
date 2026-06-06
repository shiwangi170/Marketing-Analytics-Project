import streamlit as st
import pandas as pd

st.title("👥 Customer Analytics Dashboard")

df = pd.read_csv("data/rfm_customer_segments.csv")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customers",
    df['CustomerID'].nunique()
)

col2.metric(
    "Average CLV",
    round(df['CLV'].mean(), 2)
)

col3.metric(
    "Highest CLV",
    round(df['CLV'].max(), 2)
)

st.subheader("Customer Segment Distribution")

segment_counts = df['Segment'].value_counts()

st.bar_chart(segment_counts)

st.subheader("Top 10 Customers by CLV")

top_customers = df.sort_values(
    by='CLV',
    ascending=False
).head(10)

st.dataframe(top_customers)

st.write(df.head())

st.download_button(
    label="Download Customer Data",
    data=df.to_csv(index=False),
    file_name="customer_data.csv",
    mime="text/csv"
)

customer_id = st.text_input("Enter Customer ID")

if customer_id:
    result = df[df['CustomerID'].astype(str) == customer_id]
    st.dataframe(result)


segment = st.selectbox(
    "Select Segment",
    df['Segment'].unique()
)

filtered = df[df['Segment'] == segment]

st.dataframe(filtered)

top10 = df.sort_values(
    by='CLV',
    ascending=False
).head(10)

st.dataframe(top10)

import plotly.express as px

segment_counts = df['Segment'].value_counts()

fig = px.pie(
    values=segment_counts.values,
    names=segment_counts.index,
    title="Customer Segments"
)

st.plotly_chart(fig)