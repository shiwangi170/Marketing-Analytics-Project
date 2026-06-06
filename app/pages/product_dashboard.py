import streamlit as st
import pandas as pd

st.title("🛒 Product Intelligence Dashboard")

df = pd.read_csv("data/product_recommendation_rules.csv")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Rules",
    len(df)
)

col2.metric(
    "Average Lift",
    round(df['lift'].mean(),2)
)

col3.metric(
    "Maximum Lift",
    round(df['lift'].max(),2)
)

st.subheader("Top Product Rules")

st.dataframe(
    df.sort_values(
        by='lift',
        ascending=False
    ).head(20)
)

st.subheader("Top Lift Values")

st.bar_chart(
    df.sort_values(
        by='lift',
        ascending=False
    ).head(10)['lift']
)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Rules", len(df))

col2.metric("Average Lift",
            round(df['lift'].mean(),2))

col3.metric("Max Lift",
            round(df['lift'].max(),2))

col4.metric("Average Confidence",
            round(df['confidence'].mean(),2))

top_rules = df.sort_values(
    by='lift',
    ascending=False
).head(10)

st.dataframe(top_rules)
st.bar_chart(
    top_rules.set_index('antecedents')['lift']
)

st.bar_chart(
    top_rules.set_index('antecedents')['confidence']
)

product = st.text_input(
    "Search Product"
)

if product:
    result = df[
        df['antecedents']
        .astype(str)
        .str.contains(product,
                      case=False)
    ]

    st.dataframe(result)

lift_value = st.slider(
    "Minimum Lift",
    1.0,
    float(df['lift'].max()),
    2.0
)

filtered = df[df['lift']>=lift_value]

st.dataframe(filtered)

st.subheader(
    "Top Recommendation Rules"
)

st.dataframe(
    df.sort_values(
        by='lift',
        ascending=False
    ).head(20)
)

st.success("""
Cross-Selling Opportunities

• Customers purchasing Product A
  are highly likely to purchase Product B.

• Product bundles can increase
  average basket value.

• High-lift combinations should be
  promoted together.
""")

st.download_button(
    "Download Rules",
    df.to_csv(index=False),
    "recommendation_rules.csv",
    "text/csv"
)
selected = st.selectbox(
    "Choose Product",
    sorted(df['antecedents'].astype(str).unique())
)

result = df[
    df['antecedents'].astype(str)
    == selected
]

st.dataframe(result)
st.info("""
Business Benefits

• Improve cross-selling

• Increase average order value

• Personalized product recommendations

• Better inventory planning

• Higher customer engagement
""")

st.subheader(
    "Executive Summary"
)

st.write(f"""
Total recommendation rules generated:
{len(df)}

Strongest lift value:
{df['lift'].max():.2f}

Average confidence:
{df['confidence'].mean():.2f}

These associations can be used
for recommendation systems and
marketing campaigns.
""")