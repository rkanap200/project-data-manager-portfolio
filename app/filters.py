import streamlit as st
import pandas as pd
from utils import load_data

def global_filters():
    dm, vs, ae, lb, qry, visits = load_data()

    st.sidebar.header("Filters")
    site_options = ["All"] + sorted(dm["SITEID"].unique().tolist())
    arm_options  = ["All"] + sorted(dm["ARM"].unique().tolist())
    visit_options = ["All"] + sorted(visits["VISIT"].unique().tolist())

    sites = st.sidebar.multiselect("Sites", site_options, default=["All"])
    arms  = st.sidebar.multiselect("Arms", arm_options, default=["All"])
    visits_sel = st.sidebar.multiselect("Visits", visit_options, default=["All"])

    # Date range from VISITDT
    visits_dt = pd.to_datetime(visits["VISITDT"], errors="coerce")
    start, end = visits_dt.min(), visits_dt.max()
    date_range = st.sidebar.date_input("Date range", value=(start, end))

    return (dm, vs, ae, lb, qry, visits), (sites, arms, visits_sel, date_range)
