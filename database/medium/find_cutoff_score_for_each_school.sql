-- Oracle
/* Write your PL/SQL query statement below */
with t (school_id, score, student_count, max_student_count) as (
select s.school_id, e.score, e.student_count,
       max(e.student_count) over (partition by s.school_id) as max_student_count
from schools s
     inner join exam e on (e.student_count <= s.capacity)
),
t1 (school_id, score, drnk) as (
select school_id, score,
       dense_rank() over (partition by school_id order by score) as drnk
from t
where student_count = max_student_count
)
select school_id, score
from t1
where drnk = 1
union
select school_id, -1 as score
from schools
where school_id not in (select school_id from t1)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (school_id, score, student_count, max_student_count) as (
select s.school_id, e.score, e.student_count,
       max(e.student_count) over (partition by s.school_id) as max_student_count
from schools s
     inner join exam e on (e.student_count <= s.capacity)
),
t1 (school_id, score, drnk) as (
select school_id, score,
       dense_rank() over (partition by school_id order by score) as drnk
from t
where student_count = max_student_count
)
select school_id, score
from t1
where drnk = 1
union
select school_id, -1 as score
from schools
where school_id not in (select school_id from t1)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (school_id, score, student_count, max_student_count) as (
select s.school_id, e.score, e.student_count,
       max(e.student_count) over (partition by s.school_id) as max_student_count
from schools s
     inner join exam e on (e.student_count <= s.capacity)
),
t1 (school_id, score, drnk) as (
select school_id, score,
       dense_rank() over (partition by school_id order by score) as drnk
from t
where student_count = max_student_count
)
select school_id, score
from t1
where drnk = 1
union
select school_id, -1 as score
from schools
where school_id not in (select school_id from t1)
;


# MySQL
# Write your MySQL query statement below
with t (school_id, score, student_count, max_student_count) as (
select s.school_id, e.score, e.student_count,
       max(e.student_count) over (partition by s.school_id) as max_student_count
from schools s
     inner join exam e on (e.student_count <= s.capacity)
),
t1 (school_id, score, drnk) as (
select school_id, score,
       dense_rank() over (partition by school_id order by score) as drnk
from t
where student_count = max_student_count
)
select school_id, score
from t1
where drnk = 1
union
select school_id, -1 as score
from schools
where school_id not in (select school_id from t1)
;


# Pandas
import pandas as pd

def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    df = schools.merge(exam, how='cross').query('student_count <= capacity')
    df = df.assign(
             rnk=df.groupby('school_id')['student_count'].rank(method='dense',ascending=False),
             rnk1=df.groupby(['school_id','student_count'])['score'].rank(method='dense')
         )
    df = df[(df['rnk']==1) & (df['rnk1']==1)][['school_id','score']]
    df1 = schools[~schools['school_id'].isin(df['school_id'])][['school_id']]
    df1['score'] = -1
    return pd.concat([df,df1])

