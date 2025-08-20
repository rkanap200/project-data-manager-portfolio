# Clinical Portfolio Sample (eCRFs + Dashboards)

This repo showcases a miniature clinical data management portfolio:
- **eCRF Schemas** (JSON) inspired by CDASH for common domains
- **Synthetic Trial Data** (CSV) for 100 subjects across 3 sites
- **Static eCRFs** (HTML/JS) that save responses to your browser (localStorage) for demo
- **Streamlit Dashboards** to explore KPIs (queries, enrollment, AE rates, lab flags)

## Quick Start

### Option A: View eCRFs (static)
Open the HTML files in `ecrfs_html/` directly in your browser. Submissions are stored in localStorage only (no server).

### Option B: Run dashboards
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
Then open the local URL shown by Streamlit.

## Contents
```
data/                  # synthetic CSVs
ecrf_schemas/          # JSON schemas for each eCRF
ecrfs_html/            # static demo eCRFs
app/                   # Streamlit dashboard app
sql/                   # PostgreSQL DDL (tables + basic constraints)
```

## Notes
- All data are **synthetic** and randomly generated.
- Schemas loosely align with CDASH naming conventions but are simplified for portfolio demonstration.
- The static forms are intentionally simple and front-end only; in real studies, an EDC back end, audit trail, and role-based access are required.


## Portfolio Branding
**Author:** Ragha Sudhir Kanaparthi — PMP-certified Clinical Data Manager  
**Location:** Berlin, Germany  
**Tools used:** Streamlit, Python, pandas, numpy, (Power BI/Spotfire in professional roles)




## Gallery (Static Previews)
![Subjects by Site & Arm](assets/overview_subjects_by_site_arm.png)
![Enrollment Over Time](assets/enrollment_over_time.png)
![AE Severity](assets/ae_severity.png)
![Top AE Terms](assets/ae_top_terms.png)
![Lab Out-of-Range Rate](assets/lab_out_of_range_rate.png)
![Query Aging](assets/query_aging.png)
