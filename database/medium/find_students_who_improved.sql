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
import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    df_min_ed = scores.groupby(['student_id','subject'], as_index=0)['exam_date'].min()
    df_max_ed = scores.groupby(['student_id','subject'], as_index=0)['exam_date'].max()
    df_min = ( scores
              .merge(df_min_ed, on=['student_id','subject','exam_date'], how='inner')
              .rename(columns={'score':'first_score', 'exam_date': 'first_exam_date'})
             )
    df_max = ( scores
              .merge(df_max_ed, on=['student_id','subject','exam_date'], how='inner')
              .rename(columns={'score':'latest_score', 'exam_date': 'latest_exam_date'})
             )
    return ( df_min
            .merge(df_max, on=['student_id','subject'], how='inner')
            .query('latest_exam_date > first_exam_date and latest_score > first_score')
            .sort_values(['student_id', 'subject'])[['student_id','subject','first_score','latest_score']]
           )

