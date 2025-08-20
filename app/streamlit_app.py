import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Clinical Dashboards", layout="wide")

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

@st.cache_data
def load_data():
    dm = pd.read_csv(DATA_DIR / "demographics.csv")
    vs = pd.read_csv(DATA_DIR / "vitals.csv")
    ae = pd.read_csv(DATA_DIR / "adverse_events.csv")
    lb = pd.read_csv(DATA_DIR / "labs.csv")
    qry = pd.read_csv(DATA_DIR / "query_log.csv")
    return dm, vs, ae, lb, qry

dm, vs, ae, lb, qry = load_data()

st.title("Clinical Trial KPIs — DEMO-001")

# Filters
sites = ["All"] + sorted(dm["SITEID"].unique().tolist())
site = st.selectbox("Site", sites, index=0)
arm = st.selectbox("Arm", ["All"] + sorted(dm["ARM"].unique().tolist()), index=0)

flt_dm = dm.copy()
if site != "All":
    flt_dm = flt_dm[flt_dm["SITEID"] == site]
if arm != "All":
    flt_dm = flt_dm[flt_dm["ARM"] == arm]

subj_filter = set(flt_dm["SUBJID"].tolist())
vs_f = vs[vs["SUBJID"].isin(subj_filter)]
ae_f = ae[ae["SUBJID"].isin(subj_filter)]
lb_f = lb[lb["SUBJID"].isin(subj_filter)]
qry_f = qry[qry["SUBJID"].isin(subj_filter)]

# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Subjects", len(flt_dm))
c2.metric("AE count", len(ae_f))
c3.metric("Lab High Flags", int((lb_f["LBFLAGH"]=="H").sum()))
c4.metric("Open Queries", int((qry_f["STATUS"]=="OPEN").sum()))

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["Enrollment", "Safety (AE)", "Labs", "Data Quality"])

with tab1:
    st.subheader("Enrollment by Site & Arm")
    enr = flt_dm.groupby(["SITEID","ARM"]).size().reset_index(name="N")
    st.bar_chart(enr, x="SITEID", y="N", color="ARM")
    st.caption("Counts by site and treatment arm.")

with tab2:
    st.subheader("Adverse Events")
    bysev = ae_f.groupby("AESEV").size().reindex(["MILD","MOD","SEV"]).fillna(0).reset_index(name="N")
    st.bar_chart(bysev, x="AESEV", y="N")
    st.dataframe(ae_f.sort_values("AESTDTC").head(50))

with tab3:
    st.subheader("Lab Out-of-Range Rates by Test")
    lab_rates = lb_f.assign(
        OUT=((lb_f["LBFLAGH"]=="H") | (lb_f["LBFLAGL"]=="L")).astype(int)
    ).groupby("LBTEST")["OUT"].mean().reset_index(name="OutRate")
    st.bar_chart(lab_rates, x="LBTEST", y="OutRate")
    st.dataframe(lb_f.head(50))

with tab4:
    st.subheader("Query Aging")
    qry_f["CREATED"] = pd.to_datetime(qry_f["CREATED"], errors="coerce")
    aging = qry_f.assign(
        DAYS_OPEN=(pd.Timestamp("today").normalize() - qry_f["CREATED"]).dt.days
    ).groupby("STATUS")["DAYS_OPEN"].mean().reset_index(name="AvgDaysOpen")
    st.bar_chart(aging, x="STATUS", y="AvgDaysOpen")
    st.dataframe(qry_f.head(50))

st.markdown("---")
st.caption("Synthetic demo. Built with Streamlit.")
