-- Oracle
/* Write your PL/SQL query statement below */
with student_course as (
    select s.student_id, c.course_id, c.mandatory
      from students s
           inner join courses c on (c.major = s.major)
),
student_mandatory_skip as (
    select sc.student_id
      from student_course sc
     where lower(sc.mandatory) = 'yes'
       and not exists (select null
                         from enrollments e
                        where e.student_id = sc.student_id
                          and e.course_id = sc.course_id
                      )
),
student_elective_min as (
    select sc.student_id
      from student_course sc
           left outer join enrollments e on (e.student_id = sc.student_id and e.course_id = sc.course_id)
     where lower(sc.mandatory) = 'no'
     group by sc.student_id
     having count(distinct e.course_id) < 2
),
student_mandatory_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'yes'
       and e.grade != 'A'
),
student_elective_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'no'
       and e.grade not in ('A', 'B')
),
t as (
    select e.student_id, e.course_id, e.grade, e.gpa
      from enrollments e
     where e.student_id not in (select student_id from student_mandatory_skip)
       and e.student_id not in (select student_id from student_elective_min)
       and e.student_id not in (select student_id from student_mandatory_grade)
       and e.student_id not in (select student_id from student_elective_grade)
),
t1 as (
    select student_id, avg(gpa) over (partition by student_id) as avg_gpa
      from t
)
select distinct student_id
  from t1
 where avg_gpa >= 2.5
 order by student_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with student_course as (
    select s.student_id, c.course_id, c.mandatory
      from students s
           inner join courses c on (c.major = s.major)
),
student_mandatory_skip as (
    select sc.student_id
      from student_course sc
     where lower(sc.mandatory) = 'yes'
       and not exists (select null
                         from enrollments e
                        where e.student_id = sc.student_id
                          and e.course_id = sc.course_id
                      )
),
student_elective_min as (
    select sc.student_id
      from student_course sc
           left outer join enrollments e on (e.student_id = sc.student_id and e.course_id = sc.course_id)
     where lower(sc.mandatory) = 'no'
     group by sc.student_id
     having count(distinct e.course_id) < 2
),
student_mandatory_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'yes'
       and e.grade != 'A'
),
student_elective_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'no'
       and e.grade not in ('A', 'B')
),
t as (
    select e.student_id, e.course_id, e.grade, e.gpa
      from enrollments e
     where e.student_id not in (select student_id from student_mandatory_skip)
       and e.student_id not in (select student_id from student_elective_min)
       and e.student_id not in (select student_id from student_mandatory_grade)
       and e.student_id not in (select student_id from student_elective_grade)
),
t1 as (
    select student_id, avg(gpa) over (partition by student_id) as avg_gpa
      from t
)
select distinct student_id
  from t1
 where avg_gpa >= 2.5
 order by student_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with student_course as (
    select s.student_id, c.course_id, c.mandatory
      from students s
           inner join courses c on (c.major = s.major)
),
student_mandatory_skip as (
    select sc.student_id
      from student_course sc
     where lower(sc.mandatory) = 'yes'
       and not exists (select null
                         from enrollments e
                        where e.student_id = sc.student_id
                          and e.course_id = sc.course_id
                      )
),
student_elective_min as (
    select sc.student_id
      from student_course sc
           left outer join enrollments e on (e.student_id = sc.student_id and e.course_id = sc.course_id)
     where lower(sc.mandatory) = 'no'
     group by sc.student_id
     having count(distinct e.course_id) < 2
),
student_mandatory_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'yes'
       and e.grade != 'A'
),
student_elective_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'no'
       and e.grade not in ('A', 'B')
),
t as (
    select e.student_id, e.course_id, e.grade, e.gpa
      from enrollments e
     where e.student_id not in (select student_id from student_mandatory_skip)
       and e.student_id not in (select student_id from student_elective_min)
       and e.student_id not in (select student_id from student_mandatory_grade)
       and e.student_id not in (select student_id from student_elective_grade)
),
t1 as (
    select student_id, avg(gpa) over (partition by student_id) as avg_gpa
      from t
)
select distinct student_id
  from t1
 where avg_gpa >= 2.5
 order by student_id
;


# MySQL
# Write your MySQL query statement below
with student_course as (
    select s.student_id, c.course_id, c.mandatory
      from students s
           inner join courses c on (c.major = s.major)
),
student_mandatory_skip as (
    select sc.student_id
      from student_course sc
     where lower(sc.mandatory) = 'yes'
       and not exists (select null
                         from enrollments e
                        where e.student_id = sc.student_id
                          and e.course_id = sc.course_id
                      )
),
student_elective_min as (
    select sc.student_id
      from student_course sc
           left outer join enrollments e on (e.student_id = sc.student_id and e.course_id = sc.course_id)
     where lower(sc.mandatory) = 'no'
     group by sc.student_id
     having count(distinct e.course_id) < 2
),
student_mandatory_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'yes'
       and e.grade != 'A'
),
student_elective_grade as (
    select sc.student_id
      from student_course sc
           inner join enrollments e on (e.student_id = sc.student_id and
                                        e.course_id = sc.course_id
                                       )
     where lower(sc.mandatory) = 'no'
       and e.grade not in ('A', 'B')
),
t as (
    select e.student_id, e.course_id, e.grade, e.gpa
      from enrollments e
     where e.student_id not in (select student_id from student_mandatory_skip)
       and e.student_id not in (select student_id from student_elective_min)
       and e.student_id not in (select student_id from student_mandatory_grade)
       and e.student_id not in (select student_id from student_elective_grade)
),
t1 as (
    select student_id, avg(gpa) over (partition by student_id) as avg_gpa
      from t
)
select distinct student_id
  from t1
 where avg_gpa >= 2.5
 order by student_id
;

