-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select s.student_id, c.course_id
      from students s
           inner join courses c on (c.major = s.major)
),
t1 as (
    select t.student_id, t.course_id, e.grade
      from t
           left outer join enrollments e
           on (e.student_id = t.student_id and e.course_id = t.course_id)
)
select s.student_id
  from students s
 where s.student_id not in (
                              select distinct t1.student_id
                                from t1
                               where t1.grade is null or t1.grade != 'A'
                           )
order by s.student_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select s.student_id, c.course_id
      from students s
           inner join courses c on (c.major = s.major)
),
t1 as (
    select t.student_id, t.course_id, e.grade
      from t
           left outer join enrollments e
           on (e.student_id = t.student_id and e.course_id = t.course_id)
)
select s.student_id
  from students s
 where s.student_id not in (
                              select distinct t1.student_id
                                from t1
                               where t1.grade is null or t1.grade != 'A'
                           )
order by s.student_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select s.student_id, c.course_id
      from students s
           inner join courses c on (c.major = s.major)
),
t1 as (
    select t.student_id, t.course_id, e.grade
      from t
           left outer join enrollments e
           on (e.student_id = t.student_id and e.course_id = t.course_id)
)
select s.student_id
  from students s
 where s.student_id not in (
                              select distinct t1.student_id
                                from t1
                               where t1.grade is null or t1.grade != 'A'
                           )
order by s.student_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select s.student_id, c.course_id
      from students s
           inner join courses c on (c.major = s.major)
),
t1 as (
    select t.student_id, t.course_id, e.grade
      from t
           left outer join enrollments e
           on (e.student_id = t.student_id and e.course_id = t.course_id)
)
select s.student_id
  from students s
 where s.student_id not in (
                              select distinct t1.student_id
                                from t1
                               where t1.grade is null or t1.grade != 'A'
                           )
order by s.student_id
;


# Pandas

