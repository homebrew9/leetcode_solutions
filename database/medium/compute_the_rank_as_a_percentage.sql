-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select student_id, department_id, mark,
       rank() over (partition by department_id order by mark desc) as rnk,
       count(*) over (partition by department_id) as student_count
from students
)
select student_id, department_id,
       round( case when student_count = 1 then 0
                   else ((rnk - 1) * 100) / (student_count - 1)
              end,
              2
            ) as percentage
from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select student_id, department_id, mark,
       rank() over (partition by department_id order by mark desc) as rnk,
       count(*) over (partition by department_id) as student_count
from students
)
select student_id, department_id,
       round( case when student_count = 1 then 0
                   else ((rnk - 1) * 100)::numeric / (student_count - 1)::numeric
              end,
              2
            ) as percentage
from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select student_id, department_id, mark,
       rank() over (partition by department_id order by mark desc) as rnk,
       count(*) over (partition by department_id) as student_count
from students
)
select student_id, department_id,
       round( case when student_count = 1 then 0
                   else convert(float, ((rnk - 1) * 100) )
                        /
                        convert(float, (student_count - 1) )
              end,
              2
            ) as percentage
from t
;


# MySQL
# Write your MySQL query statement below
-- Write your PostgreSQL query statement below
with t as (
select student_id, department_id, mark,
       rank() over (partition by department_id order by mark desc) as rnk,
       count(*) over (partition by department_id) as student_count
from students
)
select student_id, department_id,
       round( case when student_count = 1 then 0
                   else ((rnk - 1) * 100) / (student_count - 1)
              end,
              2
            ) as percentage
from t
;


# Pandas
import pandas as pd

def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    students['rank'] = ( students
                        .groupby('department_id', as_index=0)['mark']
                        .rank(method='min', ascending=False)
                       )
    df = ( students
          .groupby('department_id', as_index=0)['student_id']
          .count()
          .rename(columns={'student_id': 'total_count'})
         )
    df = students.merge(df, how='inner', on='department_id')
    df['percentage'] = np.where(df['total_count']==1, 0, round((df['rank'] - 1) / (df['total_count'] - 1) * 100, 2))
    return df[['student_id','department_id','percentage']].sort_values(['department_id', 'percentage'])

