import streamlit as st

st.set_page_config(page_title="Clinical Dashboards — DEMO-001", layout="wide")

st.title("Clinical Dashboards — DEMO-001")
st.caption("Ragha Sudhir Kanaparthi — PMP-certified Clinical Data Manager")
st.markdown("""
Welcome! Use the sidebar to open dashboard pages:
- **Overview**: High-level KPIs and quick counts
- **Enrollment & Retention**: Enrollment by site/arm over time
- **Safety (AEs)**: AE counts, severity mix, relatedness
- **Labs**: Out-of-range rates, per-test summaries
- **Data Quality**: Query volumes and aging
- **Subject Profile**: Drilldown for an individual subject
""")
