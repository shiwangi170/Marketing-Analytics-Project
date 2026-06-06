import streamlit as st
import pandas as pd

st.title("⚠️ Churn Dashboard")

df = pd.read_csv("data/customer_churn_predictions.csv")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Customers",
    len(df)
)

col2.metric(
    "Churn Customers",
    len(df[df['Churn']==1])
)

col3.metric(
    "Avg Churn Probability",
    round(df['Churn_Probability'].mean(),2)
)

st.subheader("High Risk Customers")

high_risk = df.sort_values(
    by='Churn_Probability',
    ascending=False
).head(20)

st.dataframe(high_risk)

st.subheader("Retention Actions")

st.bar_chart(
    df['Retention_Action'].value_counts()
)

retention_rate = ((len(df)-len(df[df['Churn']==1]))/len(df))*100

st.metric("Retention Rate", f"{retention_rate:.2f}%")

st.bar_chart(df['Churn'].value_counts())

high_risk = df.sort_values(
    by='Churn_Probability',
    ascending=False
).head(20)

st.dataframe(high_risk)

customer_id = st.text_input("Enter Customer ID")

if customer_id:
    result = df[df['CustomerID'].astype(str)==customer_id]
    st.dataframe(result)

def risk_level(x):
    if x > 0.8:
        return "High"
    elif x > 0.5:
        return "Medium"
    else:
        return "Low"

df['Risk_Level'] = df['Churn_Probability'].apply(risk_level)
st.bar_chart(df['Risk_Level'].value_counts())

segment_churn = pd.crosstab(
    df['Segment'],
    df['Churn']
)

st.dataframe(segment_churn)

high_value_risk = df[
    (df['Churn']==1)
].sort_values(
    by='CLV',
    ascending=False
).head(10)

st.dataframe(high_value_risk)

st.bar_chart(
    df['Retention_Action'].value_counts()
)

st.download_button(
    "Download High Risk Customers",
    high_risk.to_csv(index=False),
    "high_risk_customers.csv",
    "text/csv"
)

st.success("""
Business Insights

• High-risk customers should receive retention offers.

• VIP customers with churn risk need priority attention.

• Loyalty rewards can improve retention.

• Personalized marketing can reduce customer loss.
""")

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.hist(df['Churn_Probability'], bins=20)

st.pyplot(fig)

st.info("""
Key Findings:

• X customers are predicted to churn.
• Average churn probability is Y%.
• Most vulnerable segment is Z.
• Recommended retention strategy: Loyalty Program.
""")


