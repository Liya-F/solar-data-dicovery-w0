import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, get_summary_table

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title(" Cross-Country Solar Data Dashboard")

# Load Data
df = load_data()

# Country Selector
countries = st.multiselect("Select countries to view", df['Country'].unique(), default=df['Country'].unique())

filtered_df = df[df['Country'].isin(countries)]

# Metric Selector
metric = st.selectbox("Choose metric to visualize", ["GHI", "DNI", "DHI"])

# Boxplot
st.subheader(f"Distribution of {metric} by Country")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=filtered_df, x="Country", y=metric, ax=ax, palette="Set2")
st.pyplot(fig)

# Summary Table
st.subheader(" Summary Statistics Table")
st.dataframe(get_summary_table(filtered_df))

st.markdown("---")
st.caption("Built with Streamlit | Solar Data © 2025")
