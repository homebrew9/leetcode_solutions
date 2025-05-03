-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
select q.id, q.year, coalesce(n.npv, 0) as npv
  from queries q
       left outer join npv n on (n.id = q.id and n.year = q.year)
;

# Pandas
import pandas as pd

def npv_queries(npv: pd.DataFrame, queries: pd.DataFrame) -> pd.DataFrame:
    return queries.merge(npv, how='left', on=['id','year']).fillna(0)

