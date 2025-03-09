-- Oracle
/* Write your PL/SQL query statement below */
--
with t (exam_id, student_id, score, rank_from_top, rank_from_bottom) as (
    select exam_id, student_id, score,
           dense_rank() over (partition by exam_id order by score desc) as rank_from_top,
           dense_rank() over (partition by exam_id order by score) as rank_from_bottom
      from exam
)
select s.student_id, s.student_name
  from student s
 where exists (select null
                 from exam e
                where e.student_id = s.student_id
              )
   and not exists (select null
                     from t
                    where t.student_id = s.student_id
                      and (t.rank_from_top = 1 or t.rank_from_bottom = 1)
                  )
 order by s.student_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (exam_id, student_id, score, rank_from_top, rank_from_bottom) as (
select exam_id, student_id, score,
       dense_rank() over (partition by exam_id order by score desc) as rank_from_top,
       dense_rank() over (partition by exam_id order by score) as rank_from_bottom
from exam
),
x (student_id) as (
select distinct t1.student_id
from t t1
where t1.rank_from_top != 1
and t1.rank_from_bottom != 1
and not exists (
    select null
    from t t2
    where t2.student_id = t1.student_id
    and (t2.rank_from_top = 1 or t2.rank_from_bottom = 1)
)
)
select s.student_id, s.student_name
from student s
     inner join x on (x.student_id = s.student_id)
order by s.student_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (exam_id, student_id, score, rank_from_top, rank_from_bottom) as (
select exam_id, student_id, score,
       dense_rank() over (partition by exam_id order by score desc) as rank_from_top,
       dense_rank() over (partition by exam_id order by score) as rank_from_bottom
from exam
),
x (student_id) as (
select distinct t1.student_id
from t t1
where t1.rank_from_top != 1
and t1.rank_from_bottom != 1
and not exists (
    select null
    from t t2
    where t2.student_id = t1.student_id
    and (t2.rank_from_top = 1 or t2.rank_from_bottom = 1)
)
)
select s.student_id, s.student_name
from student s
     inner join x on (x.student_id = s.student_id)
order by s.student_id
;


# MySQL
# Write your MySQL query statement below
with t (exam_id, student_id, score, rank_from_top, rank_from_bottom) as (
select exam_id, student_id, score,
       dense_rank() over (partition by exam_id order by score desc) as rank_from_top,
       dense_rank() over (partition by exam_id order by score) as rank_from_bottom
from exam
),
x (student_id) as (
select distinct t1.student_id
from t t1
where t1.rank_from_top != 1
and t1.rank_from_bottom != 1
and not exists (
    select null
    from t t2
    where t2.student_id = t1.student_id
    and (t2.rank_from_top = 1 or t2.rank_from_bottom = 1)
)
)
select s.student_id, s.student_name
from student s
     inner join x on (x.student_id = s.student_id)
order by s.student_id
;


# Pandas
import pandas as pd

def find_quiet_students(student: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    exam_takers = exam['student_id'].drop_duplicates()
    highest_or_lowest = ( exam
                         .assign(rnk=exam.groupby('exam_id')['score'].rank(method='dense'))
                         .assign(rnk1=exam.groupby('exam_id')['score'].rank(method='dense',ascending=False))
                         .query('rnk==1 or rnk1==1')['student_id']
                         .drop_duplicates()
                        )
    return ( student[
                 (student['student_id'].isin(exam_takers))
                  &
                 (~student['student_id'].isin(highest_or_lowest))
             ]
           )

