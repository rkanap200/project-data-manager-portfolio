import streamlit as st
import pandas as pd
from filters import global_filters
from utils import apply_filters

st.title("Data Quality — Queries")
(data, sel) = global_filters()
(dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range) = data, sel
flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f = apply_filters(dm, vs, ae, lb, qry, visits, sites, arms, visits_sel, date_range)

if not qry_f.empty:
    qry_f["CREATED"] = pd.to_datetime(qry_f["CREATED"], errors="coerce")
    aging = qry_f.assign(DAYS_OPEN=(pd.Timestamp('today').normalize() - qry_f["CREATED"]).dt.days)
    st.subheader("Average Days Open by Status")
    avg = aging.groupby("STATUS")["DAYS_OPEN"].mean().reset_index(name="AvgDaysOpen")
    st.bar_chart(avg, x="STATUS", y="AvgDaysOpen")

    st.subheader("Query Volume by Site")
    by_site = qry_f.groupby("SUBJID").size().reset_index(name="N")
    # Map subjid to site
    dm_map = dm[["SUBJID","SITEID"]].drop_duplicates()
    by_site = by_site.merge(dm_map, on="SUBJID", how="left").groupby("SITEID")["N"].sum().reset_index()
    st.bar_chart(by_site, x="SITEID", y="N")
    st.dataframe(qry_f.head(100))
else:
    st.info("No queries after filters.")
