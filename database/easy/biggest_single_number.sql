-- Oracle
/* Write your PL/SQL query statement below */
with t (num, num_occurrences) as (
select num, count(*) over (partition by num) as num_occurrences
from MyNumbers
)
select max(num) as num
from t
where num_occurrences = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (num, frequency) as (
    select num, count(*) as frequency
      from mynumbers
     group by num
)
select max(num) as num
  from t
 where frequency = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (num, frequency) as (
    select num, count(*) as frequency
      from mynumbers
     group by num
)
select max(num) as num
  from t
 where frequency = 1
;


# MySQL
# Write your MySQL query statement below
with t (num, frequency) as (
    select num, count(*) as frequency
      from mynumbers
     group by num
)
select max(num) as num
  from t
 where frequency = 1
;


# Pandas
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
               'num': [
                         my_numbers['num']
                        .value_counts()
                        .to_frame()
                        .query('count==1')
                        .index
                        .max()
                      ]
            })

