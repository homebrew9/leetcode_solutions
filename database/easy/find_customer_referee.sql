-- Oracle
/* Write your PL/SQL query statement below */
select name
from customer
where referee_id is null or referee_id != 2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select name
  from customer
 where referee_id is null or referee_id <> 2
;


-- SQL Server
/* Write your T-SQL query statement below */
select name
from customer
where isnull(referee_id, 0) != 2;


# MySQL
# Write your MySQL query statement below
select name
from customer
where coalesce(referee_id, -1) != 2
;


# Pandas
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer['referee_id'].isna()) | (customer['referee_id'] != 2)][['name']]

