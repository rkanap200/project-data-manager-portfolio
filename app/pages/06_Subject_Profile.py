import streamlit as st
import pandas as pd
from filters import global_filters
from utils import apply_filters

st.title("Subject Profile")
(data, sel) = global_filters()
(dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range) = data, sel

subj = st.selectbox("Select Subject", sorted(dm["SUBJID"].unique()))
flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f = apply_filters(dm, vs, ae, lb, qry, visits, sites, arms, visits_sel, date_range, subjid=subj)

st.subheader("Demographics")
st.dataframe(flt_dm)

st.subheader("Visits")
st.dataframe(visits_f.sort_values("VISITDT"))

st.subheader("Vitals")
st.dataframe(vs_f.sort_values("VSDTC"))

st.subheader("AEs")
st.dataframe(ae_f.sort_values("AESTDTC"))

st.subheader("Labs (recent 50)")
st.dataframe(lb_f.sort_values("LBDTC").head(50))

st.subheader("Queries")
st.dataframe(qry_f)
