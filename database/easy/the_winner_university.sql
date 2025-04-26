-- Oracle
/* Write your PL/SQL query statement below */
select case when ny.student_count = ca.student_count then 'No Winner'
            when ny.student_count > ca.student_count then 'New York University'
            when ca.student_count > ny.student_count then 'California University'
       end as winner
  from (select count(*) as student_count from NewYork where score >= 90) ny
       cross join
       (select count(*) as student_count from California where score >= 90) ca
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select case when ny.student_count = ca.student_count then 'No Winner'
            when ny.student_count > ca.student_count then 'New York University'
            when ca.student_count > ny.student_count then 'California University'
       end as winner
  from (select count(*) as student_count from NewYork where score >= 90) ny
       cross join
       (select count(*) as student_count from California where score >= 90) ca
;


-- SQL Server
/* Write your T-SQL query statement below */
select case when ny.student_count = ca.student_count then 'No Winner'
            when ny.student_count > ca.student_count then 'New York University'
            when ca.student_count > ny.student_count then 'California University'
       end as winner
  from (select count(*) as student_count from NewYork where score >= 90) ny
       cross join
       (select count(*) as student_count from California where score >= 90) ca
;


# MySQL
# Write your MySQL query statement below
select case when ny.student_count = ca.student_count then 'No Winner'
            when ny.student_count > ca.student_count then 'New York University'
            when ca.student_count > ny.student_count then 'California University'
       end as winner
  from (select count(*) as student_count from NewYork where score >= 90) ny
       cross join
       (select count(*) as student_count from California where score >= 90) ca
;


# Pandas
import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    ny = new_york[new_york['score'] >= 90]['student_id'].count()
    ca = california[california['score'] >= 90]['student_id'].count()
    if ny == ca:
        val = 'No Winner'
    elif ny > ca:
        val = 'New York University'
    else:
        val = 'California University'
    return pd.DataFrame(data=[val], columns=['winner'])

