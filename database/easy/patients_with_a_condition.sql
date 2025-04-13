-- Oracle
/* Write your PL/SQL query statement below */
select patient_id, patient_name, conditions
from patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select patient_id, patient_name, conditions
  from patients
 where lower(conditions) like 'diab1%' or lower(conditions) like '% diab1%'
;


-- SQL Server
/* Write your T-SQL query statement below */
select patient_id, patient_name, conditions
  from patients
 where lower(conditions) like 'diab1%' or lower(conditions) like '% diab1%'
;


# MySQL
# Write your MySQL query statement below
select patient_id, patient_name, conditions
  from patients
-- where lower(conditions) like 'diab1%' or lower(conditions) like '% diab1%'
 where regexp_like(conditions, '(^| )diab1.*$')
;


# Pandas
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(^DIAB1)|( DIAB1)', na=False)]

