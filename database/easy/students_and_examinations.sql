-- Oracle
/* Write your PL/SQL query statement below */
with t (student_id, student_name, subject_name, attended_exams) as (
select student_id, student_name, subject_name, 0
from students
     cross join subjects
),
t1 (student_id, student_name, subject_name, attended_exams) as (
select distinct s.student_id, s.student_name, sb.subject_name,
       count(*) over (partition by s.student_id, sb.subject_name) as attended_exams
from examinations e
     inner join students s on (s.student_id = e.student_id)
     inner join subjects sb on (sb.subject_name = e.subject_name)
),
t2 (student_id, student_name, subject_name, attended_exams) as (
select student_id, student_name, subject_name, attended_exams
from t1
union all
select student_id, student_name, subject_name, attended_exams
from t
where not exists (select null from t1 where t1.student_id = t.student_id and t1.subject_name = t.subject_name)
)
select student_id, student_name, subject_name, attended_exams
from t2
order by student_id, subject_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (student_id, student_name, subject_name) as (
    select student_id, student_name, subject_name
      from students
           cross join subjects
),
t1 (student_id, subject_name, attended_exams) as (
    select student_id, subject_name, count(*) as attended_exams
      from examinations e
     group by student_id, subject_name
)
select t.student_id,
       t.student_name,
       t.subject_name,
       coalesce(t1.attended_exams, 0) as attended_exams
  from t
       left outer join t1 on (t1.student_id = t.student_id and t1.subject_name = t.subject_name)
 order by t.student_id, t.subject_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (student_id, student_name, subject_name) as (
    select student_id, student_name, subject_name
      from students
           cross join subjects
),
t1 (student_id, subject_name, attended_exams) as (
    select student_id, subject_name, count(*) as attended_exams
      from examinations e
     group by student_id, subject_name
)
select t.student_id,
       t.student_name,
       t.subject_name,
       coalesce(t1.attended_exams, 0) as attended_exams
  from t
       left outer join t1 on (t1.student_id = t.student_id and t1.subject_name = t.subject_name)
 order by t.student_id, t.subject_name
;


# MySQL
# Write your MySQL query statement below
with t (student_id, student_name, subject_name) as (
    select student_id, student_name, subject_name
      from students
           cross join subjects
),
t1 (student_id, subject_name, attended_exams) as (
    select student_id, subject_name, count(*) as attended_exams
      from examinations e
     group by student_id, subject_name
)
select t.student_id,
       t.student_name,
       t.subject_name,
       coalesce(t1.attended_exams, 0) as attended_exams
  from t
       left outer join t1 on (t1.student_id = t.student_id and t1.subject_name = t.subject_name)
 order by t.student_id, t.subject_name
;


# Pandas
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = examinations.groupby(
             ['student_id','subject_name'],as_index=False
         ).agg(
             attended_exams=('student_id','count')
         )
    return students.merge(
               subjects, how='cross'
           ).merge(
               df, how='left', on=['student_id','subject_name']
           ).fillna(0)[['student_id','student_name','subject_name','attended_exams']].sort_values(
               ['student_id','subject_name']
           )

