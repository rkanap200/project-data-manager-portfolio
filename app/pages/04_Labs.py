import streamlit as st
import pandas as pd
from filters import global_filters
from utils import apply_filters

st.title("Laboratory Assessments")
(data, sel) = global_filters()
(dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range) = data, sel
flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f = apply_filters(dm, vs, ae, lb, qry, visits, sites, arms, visits_sel, date_range)

st.subheader("Out-of-Range Rate by Test")
if not lb_f.empty:
    lb_f["OUT"] = ((lb_f["LBFLAGH"]=="H") | (lb_f["LBFLAGL"]=="L")).astype(int)
    rates = lb_f.groupby("LBTEST")["OUT"].mean().reset_index(name="OutRate")
    st.bar_chart(rates, x="LBTEST", y="OutRate")
    st.dataframe(lb_f.head(100))
else:
    st.info("No lab data after filters.")
