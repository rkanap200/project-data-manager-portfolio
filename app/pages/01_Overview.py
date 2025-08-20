import streamlit as st
import pandas as pd
from filters import global_filters
from utils import apply_filters

st.title("Overview")
(data, sel) = global_filters()
(dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range) = data, sel
flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f = apply_filters(dm, vs, ae, lb, qry, visits, sites, arms, visits_sel, date_range)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Subjects", len(flt_dm))
c2.metric("AEs", len(ae_f))
c3.metric("Lab High Flags", int((lb_f.get("LBFLAGH","")=="H").sum()) if "LBFLAGH" in lb_f.columns else 0)
c4.metric("Open Queries", int((qry_f.get("STATUS","")=="OPEN").sum()) if "STATUS" in qry_f.columns else 0)

st.markdown("---")
st.subheader("Subjects by Site & Arm")
enr = flt_dm.groupby(["SITEID","ARM"]).size().reset_index(name="N")
st.bar_chart(enr, x="SITEID", y="N", color="ARM")
