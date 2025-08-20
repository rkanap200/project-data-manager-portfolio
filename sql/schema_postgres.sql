
-- PostgreSQL DDL for the demo study
CREATE TABLE dm (
  studyid text, siteid text, subjid text PRIMARY KEY, arm text, sex text CHECK (sex IN ('M','F')), age int CHECK (age BETWEEN 18 AND 90), icf_date date
);
CREATE TABLE visits (
  studyid text, subjid text, visit text, visitdt date,
  PRIMARY KEY (subjid, visit),
  FOREIGN KEY (subjid) REFERENCES dm(subjid)
);
CREATE TABLE vs (
  studyid text, subjid text, visit text, vsdtc date, hr int, sbp int, dbp int, weight_kg numeric, height_cm numeric,
  PRIMARY KEY (subjid, visit),
  FOREIGN KEY (subjid) REFERENCES dm(subjid)
);
CREATE TABLE ae (
  studyid text, subjid text, aedecod text, aestdtc date, aeendtc date, aesev text, aerel text, aeser text,
  PRIMARY KEY (subjid, aedecod, aestdtc),
  FOREIGN KEY (subjid) REFERENCES dm(subjid)
);
CREATE TABLE cm (
  studyid text, subjid text, cmtrt text, cmindc text, cmstdtc date, cmongo text,
  PRIMARY KEY (subjid, cmtrt, cmstdtc),
  FOREIGN KEY (subjid) REFERENCES dm(subjid)
);
CREATE TABLE lb (
  studyid text, subjid text, visit text, lbdtc date, lbtest text, lborres numeric, lbnrlo numeric, lbnrhi numeric, lbflagh text, lbflagl text,
  PRIMARY KEY (subjid, visit, lbtest, lbdtc),
  FOREIGN KEY (subjid) REFERENCES dm(subjid)
);
CREATE TABLE qry (
  studyid text, subjid text, domain text, record_key text, query_text text, status text, created date
);
