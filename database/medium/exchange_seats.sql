-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select id, student,
           lead(student) over (order by id) as next_student,
           lag(student) over (order by id) as prev_student
      from seat
)
select id,
       nvl(case when mod(id, 2) = 1 then next_student else prev_student end, student) as student
  from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select id, student,
           lead(student) over (order by id) as next_student,
           lag(student) over (order by id) as prev_student
      from seat
)
select id,
       coalesce(case when mod(id, 2) = 1 then next_student else prev_student end, student) as student
  from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select id, student,
           lead(student) over (order by id) as next_student,
           lag(student) over (order by id) as prev_student
      from seat
)
select id,
       coalesce(case when id % 2 = 1 then next_student else prev_student end, student) as student
  from t
;


# MySQL
# Write your MySQL query statement below
--
select s1.id as id,
       coalesce(s2.student, s1.student) as student
  from seat s1
       left outer join seat s2 on
       (
            (mod(s1.id, 2) = 1 and s1.id = s2.id - 1) or
            (mod(s1.id, 2) = 0 and s1.id = s2.id + 1)
       )
 order by s1.id
;


# Pandas
import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat['swap_id'] = np.where(seat['id'] % 2 == 0, seat['id'] - 1, seat['id'] + 1)
    df = seat.merge(seat, how='left', left_on='swap_id', right_on='id')
    df['student_y'] = np.where(df['student_y'].isna(), df['student_x'], df['student_y'])
    return df[['id_x','student_y']].rename(columns={'id_x':'id', 'student_y':'student'})

