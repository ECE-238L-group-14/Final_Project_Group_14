import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------
# PAGE CONFIG
# --------------------
st.set_page_config(
    page_title="Education Dashboard",
    page_icon="🎓",
    layout="wide"
)

# --------------------
# DATA
# --------------------

edu_18_24 = [
    "Less than High School",
    "High School Graduate",
    "Some College / Associate",
    "Bachelor's Degree or Higher"
]

data_18_24 = [20.4, 51.2, 28.2, 0.2]

edu_25_plus = [
    "Less than 9th Grade",
    "9th-12th Grade, No Diploma",
    "High School Graduate",
    "Some College, No Degree",
    "Associate Degree",
    "Bachelor's Degree",
    "Graduate/Professional Degree"
]

data_25_plus = [7.5, 18.4, 37.6, 20.6, 5.6, 6.8, 3.5]

# --------------------
# SIDEBAR
# --------------------

st.sidebar.title("Dashboard Controls")

age_group = st.sidebar.selectbox(
    "Select Age Group",
    ["18-24 Years", "25+ Years"]
)

# --------------------
# DATAFRAME
# --------------------

if age_group == "18-24 Years":
    df = pd.DataFrame({
        "Education": edu_18_24,
        "Percentage": data_18_24
    })

    title = "Population Ages 18-24 by Education Level"
    max_y = 60

else:
    df = pd.DataFrame({
        "Education": edu_25_plus,
        "Percentage": data_25_plus
    })

    title = "Population Ages 25+ by Education Level"
    max_y = 45

# --------------------
# HEADER
# --------------------

st.title("🎓 Education Attainment Dashboard")
st.markdown(
    "Interactive visualization of educational attainment percentages by age group."
)

# --------------------
# METRICS
# --------------------

col1, col2, col3 = st.columns(3)

highest = df.loc[df["Percentage"].idxmax()]

col1.metric(
    "Highest Category",
    highest["Education"]
)

col2.metric(
    "Highest %",
    f"{highest['Percentage']}%"
)

col3.metric(
    "Average %",
    f"{df['Percentage'].mean():.1f}%"
)

# --------------------
# CHART
# --------------------

fig = px.bar(
    df,
    x="Education",
    y="Percentage",
    text="Percentage",
    color="Percentage",
    color_continuous_scale="Blues",
)

fig.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig.update_layout(
    title=title,
    xaxis_title="Education Level",
    yaxis_title="Percentage (%)",
    yaxis=dict(range=[0, max_y]),
    template="plotly_white",
    height=600,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# --------------------
# TABLE
# --------------------

st.subheader("Data Table")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

# --------------------
# INSIGHTS
# --------------------

st.subheader("Insights")

st.info(
    f"""
    • Largest category: {highest['Education']} ({highest['Percentage']}%)

    • Total categories analyzed: {len(df)}

    • Average percentage across categories:
      {df['Percentage'].mean():.1f}%
    """
)

