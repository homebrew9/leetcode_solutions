-- Oracle
/* Write your PL/SQL query statement below */
-- Without analytic functions
select x.student_id, x.subject, x.first_score, y.latest_score
  from (
            select s.student_id, s.subject, s.exam_date, s.score as first_score
            from scores s
            where s.exam_date = (select min(s1.exam_date)
                                   from scores s1
                                  where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) x
inner join
       (
            select s.student_id, s.subject, s.exam_date, s.score as latest_score
            from scores s
            where s.exam_date = (select max(s1.exam_date)
                                    from scores s1
                                    where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) y
    on (x.student_id = y.student_id and x.subject = y.subject)
 where y.exam_date > x.exam_date
   and y.latest_score > x.first_score
 order by x.student_id, x.subject
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- Without analytic functions
select x.student_id, x.subject, x.first_score, y.latest_score
  from (
            select s.student_id, s.subject, s.exam_date, s.score as first_score
            from scores s
            where s.exam_date = (select min(s1.exam_date)
                                   from scores s1
                                  where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) x
inner join
       (
            select s.student_id, s.subject, s.exam_date, s.score as latest_score
            from scores s
            where s.exam_date = (select max(s1.exam_date)
                                    from scores s1
                                    where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) y
    on (x.student_id = y.student_id and x.subject = y.subject)
 where y.exam_date > x.exam_date
   and y.latest_score > x.first_score
 order by x.student_id, x.subject
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Without analytic functions
select x.student_id, x.subject, x.first_score, y.latest_score
  from (
            select s.student_id, s.subject, s.exam_date, s.score as first_score
            from scores s
            where s.exam_date = (select min(s1.exam_date)
                                   from scores s1
                                  where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) x
inner join
       (
            select s.student_id, s.subject, s.exam_date, s.score as latest_score
            from scores s
            where s.exam_date = (select max(s1.exam_date)
                                    from scores s1
                                    where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) y
    on (x.student_id = y.student_id and x.subject = y.subject)
 where y.exam_date > x.exam_date
   and y.latest_score > x.first_score
 order by x.student_id, x.subject
;


# MySQL
# Write your MySQL query statement below
-- Without analytic functions
select x.student_id, x.subject, x.first_score, y.latest_score
  from (
            select s.student_id, s.subject, s.exam_date, s.score as first_score
            from scores s
            where s.exam_date = (select min(s1.exam_date)
                                   from scores s1
                                  where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) x
inner join
       (
            select s.student_id, s.subject, s.exam_date, s.score as latest_score
            from scores s
            where s.exam_date = (select max(s1.exam_date)
                                    from scores s1
                                    where s1.student_id = s.student_id
                                    and s1.subject = s.subject
                                )
       ) y
    on (x.student_id = y.student_id and x.subject = y.subject)
 where y.exam_date > x.exam_date
   and y.latest_score > x.first_score
 order by x.student_id, x.subject
;


# Pandas

