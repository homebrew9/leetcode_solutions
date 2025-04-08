-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select student_id, course_id, grade,
           dense_rank() over (partition by student_id order by grade desc, course_id) as drnk
      from enrollments
)
select student_id, course_id, grade
  from t
 where drnk = 1
 order by student_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select student_id, course_id, grade
from (
select student_id, course_id, grade,
       dense_rank() over (partition by student_id order by grade desc, course_id) as drnk
from enrollments
) t
where drnk = 1
order by student_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select student_id, course_id, grade
from (
select student_id, course_id, grade,
       dense_rank() over (partition by student_id order by grade desc, course_id) as drnk
from enrollments
) t
where drnk = 1
order by student_id
;


# MySQL
# Write your MySQL query statement below
select student_id, course_id, grade
from (
select student_id, course_id, grade,
       dense_rank() over (partition by student_id order by grade desc, course_id) as drnk
from enrollments
) t
where drnk = 1
order by student_id
;


# Pandas
import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    df = (  enrollments
           .groupby('student_id',as_index=False)['grade']
           .max()
           .rename(columns={'grade':'max_grade'})
         )
    return (  enrollments
             .merge(df, how='inner', on='student_id')
             .query('grade == max_grade')
             .groupby('student_id',as_index=False)
             .agg({'course_id': 'min','grade':'max'})
             .sort_values('student_id')
           )

