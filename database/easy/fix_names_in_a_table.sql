-- Oracle
/* Write your PL/SQL query statement below */
select user_id, upper(substr(name,1,1)) || lower(substr(name,2,length(name))) as "name"
from users
order by user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select user_id, upper(substring(name, 1, 1))||lower(substring(name,2)) as name
from users
order by user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select user_id, upper(substring(name, 1, 1)) + lower(substring(name,2,len(name))) as name
from users
order by user_id
;


# MySQL
# Write your MySQL query statement below
select user_id,
       concat(upper(substring(name, 1, 1)), lower(substring(name,2))) as name
from users
order by user_id
;


# Pandas
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')

