-- Oracle
/* Write your PL/SQL query statement below */
select to_char(date_id, 'YYYY-MM-DD') as date_id,
       make_name,
       count(distinct lead_id) as unique_leads,
       count(distinct partner_id) as unique_partners
  from DailySales
 group by date_id, make_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select date_id, make_name,
       count(distinct lead_id) as unique_leads,
       count(distinct partner_id) as unique_partners
from dailysales
group by date_id, make_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select date_id, make_name,
       count(distinct lead_id) as unique_leads,
       count(distinct partner_id) as unique_partners
from dailysales
group by date_id, make_name
;


# MySQL
# Write your MySQL query statement below
select date_id, make_name,
       count(distinct lead_id) as unique_leads,
       count(distinct partner_id) as unique_partners
from dailysales
group by date_id, make_name
;


# Pandas
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(
               ['date_id','make_name'],
               as_index=False
           ).nunique().rename(
               columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}
           )

