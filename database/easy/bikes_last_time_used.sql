-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
select bike_number, max(end_time) as end_time
from bikes
group by bike_number
order by end_time desc
;


-- SQL Server
/* Write your T-SQL query statement below */
select bike_number, max(end_time) as end_time
from bikes
group by bike_number
order by end_time desc
;


# MySQL
# Write your MySQL query statement below
select bike_number, max(end_time) as end_time
from bikes
group by bike_number
order by end_time desc
;


# Pandas
import pandas as pd

def last_used_time(bikes: pd.DataFrame) -> pd.DataFrame:
    return ( bikes
            .groupby('bike_number', as_index=False)['end_time']
            .max()
            .sort_values(by='end_time', ascending=False)
           )

