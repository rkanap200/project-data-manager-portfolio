import streamlit as st
import pandas as pd
from filters import global_filters
from utils import apply_filters

st.title("Enrollment & Retention")
(data, sel) = global_filters()
(dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range) = data, sel
flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f = apply_filters(dm, vs, ae, lb, qry, visits, sites, arms, visits_sel, date_range)

# Enrollment over time (Baseline)
st.subheader("Enrollment Over Time")
visits_f["VISITDT"] = pd.to_datetime(visits_f["VISITDT"], errors="coerce")
enr_time = visits_f[visits_f["VISIT"] == "BASELINE"].groupby(visits_f["VISITDT"].dt.to_period("W")).size()
enr_time.index = enr_time.index.to_timestamp()
st.line_chart(enr_time)

# Screening vs Baseline by Site
st.subheader("Screening vs Baseline Counts by Site")

# 🔑 FIX: add SITEID from demographics (dm)
dm_map = dm[["SUBJID", "SITEID"]].drop_duplicates()
vf = visits_f.merge(dm_map, on="SUBJID", how="left")

counts = vf[vf["VISIT"].isin(["SCREEN", "BASELINE"])].groupby(["SITEID", "VISIT"]).size().reset_index(name="N")
st.bar_chart(counts, x="SITEID", y="N", color="VISIT")
