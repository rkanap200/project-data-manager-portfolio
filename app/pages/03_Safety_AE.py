import streamlit as st
import pandas as pd
from filters import global_filters
from utils import apply_filters

st.title("Safety — Adverse Events")
(data, sel) = global_filters()
(dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range) = data, sel
flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f = apply_filters(dm, vs, ae, lb, qry, visits, sites, arms, visits_sel, date_range)

st.subheader("AEs by Severity")
by_sev = ae_f.groupby("AESEV").size().reindex(["MILD","MOD","SEV"]).fillna(0).reset_index(name="N")
st.bar_chart(by_sev, x="AESEV", y="N")

st.subheader("AEs by Relatedness")
if "AEREL" in ae_f.columns:
    by_rel = ae_f.groupby("AEREL").size().reset_index(name="N")
    st.bar_chart(by_rel, x="AEREL", y="N")

st.subheader("Top AE Terms")
if "AEDECOD" in ae_f.columns:
    top_terms = ae_f["AEDECOD"].value_counts().reset_index()
    top_terms.columns = ["AEDECOD","N"]
    st.bar_chart(top_terms.head(10), x="AEDECOD", y="N")
st.dataframe(ae_f.sort_values("AESTDTC").head(100))
