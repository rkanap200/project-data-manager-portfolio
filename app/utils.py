import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_data():
    dm = pd.read_csv(DATA_DIR / "demographics.csv")
    vs = pd.read_csv(DATA_DIR / "vitals.csv")
    ae = pd.read_csv(DATA_DIR / "adverse_events.csv")
    lb = pd.read_csv(DATA_DIR / "labs.csv")
    qry = pd.read_csv(DATA_DIR / "query_log.csv")
    visits = pd.read_csv(DATA_DIR / "visits.csv")
    return dm, vs, ae, lb, qry, visits

def apply_filters(dm, vs, ae, lb, qry, visits, sites=None, arms=None, visits_sel=None, date_range=None, subjid=None):
    # Sites / Arms
    flt_dm = dm.copy()
    if sites and "All" not in sites:
        flt_dm = flt_dm[flt_dm["SITEID"].isin(sites)]
    if arms and "All" not in arms:
        flt_dm = flt_dm[flt_dm["ARM"].isin(arms)]

    subj_filter = set(flt_dm["SUBJID"].tolist())
    vs_f = vs[vs["SUBJID"].isin(subj_filter)].copy()
    ae_f = ae[ae["SUBJID"].isin(subj_filter)].copy()
    lb_f = lb[lb["SUBJID"].isin(subj_filter)].copy()
    qry_f = qry[qry["SUBJID"].isin(subj_filter)].copy()
    visits_f = visits[visits["SUBJID"].isin(subj_filter)].copy()

    # Visit filter
    if visits_sel and "All" not in visits_sel:
        vs_f = vs_f[vs_f["VISIT"].isin(visits_sel)]
        lb_f = lb_f[lb_f["VISIT"].isin(visits_sel)]
        visits_f = visits_f[visits_f["VISIT"].isin(visits_sel)]

    # Date filter
    if date_range and len(date_range) == 2:
        start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        for df, col in [(vs_f,"VSDTC"), (ae_f,"AESTDTC"), (lb_f,"LBDTC"), (visits_f,"VISITDT")]:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors="coerce")
                df.dropna(subset=[col], inplace=True)
                df.query(f"{col} >= @start and {col} <= @end", inplace=True)

    # Subject filter (for profile page)
    if subjid:
        flt_dm = flt_dm[flt_dm["SUBJID"] == subjid]
        vs_f = vs_f[vs_f["SUBJID"] == subjid]
        ae_f = ae_f[ae_f["SUBJID"] == subjid]
        lb_f = lb_f[lb_f["SUBJID"] == subjid]
        qry_f = qry_f[qry_f["SUBJID"] == subjid]
        visits_f = visits_f[visits_f["SUBJID"] == subjid]

    return flt_dm, vs_f, ae_f, lb_f, qry_f, visits_f
