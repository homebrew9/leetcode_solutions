-- Oracle
/* Write your PL/SQL query statement below */
with t_session_detail as (
    select session_id, student_id, subject, session_date, hours_studied,
           dense_rank() over (partition by student_id order by session_date) as drnk,
           count(*) over (partition by student_id) as total_session_length,
           session_date - lag(session_date) over (partition by student_id order by session_date) as session_gap
      from study_sessions
),
t_valid_students as (
    select distinct ss.student_id
      from study_sessions ss
     where not exists (select null
                         from t_session_detail sd
                        where sd.student_id = ss.student_id
                          and (sd.session_gap > 2 or sd.total_session_length < 6)
                      )
),
t_sessions_cmp as (
    select sd.session_id, sd.student_id, sd.subject, sd.session_date, sd.hours_studied,
           sd.drnk, sd.total_session_length, sd.session_gap,
           sd1.session_date as session_date1, sd1.drnk as drnk1, sd1.hours_studied as hs1,
           sd1.drnk
           - 
           lag(sd1.drnk) over (partition by sd.student_id, sd.subject order by sd1.session_date) as rank_offset
      from t_session_detail sd
           inner join t_valid_students vs on (vs.student_id = sd.student_id)
           inner join t_session_detail sd1 on (sd1.student_id = sd.student_id and sd1.subject = sd.subject)
),
t_dist_ro as (
    select session_id, student_id, subject, session_date, hours_studied, drnk,
           total_session_length, session_gap, session_date1, drnk1, hs1, rank_offset,
           count(distinct rank_offset) over (partition by student_id) as dist_rank_offset
      from t_sessions_cmp
     where rank_offset is null or rank_offset != 0
)
,
t_study_cycle as (
    select student_id,
           count(distinct subject) as cycle_length,
           sum(hs1) as total_study_hours
      from t_dist_ro
     where dist_rank_offset = 1
     group by student_id
    having count(distinct subject) >= 3
)
select sc.student_id, s.student_name, s.major, sc.cycle_length, sc.total_study_hours
  from t_study_cycle sc
       inner join students s on (s.student_id = sc.student_id)
 order by sc.cycle_length desc, sc.total_study_hours desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t_session_detail as (
    select session_id, student_id, subject, session_date, hours_studied,
           dense_rank() over (partition by student_id order by session_date) as drnk,
           count(*) over (partition by student_id) as total_session_length,
           session_date - lag(session_date) over (partition by student_id order by session_date) as session_gap
      from study_sessions
),
t_valid_students as (
    select distinct ss.student_id
      from study_sessions ss
     where not exists (select null
                         from t_session_detail sd
                        where sd.student_id = ss.student_id
                          and (sd.session_gap > 2 or sd.total_session_length < 6)
                      )
),
t_sessions_cmp as (
    select sd.session_id, sd.student_id, sd.subject, sd.session_date, sd.hours_studied,
           sd.drnk, sd.total_session_length, sd.session_gap,
           sd1.session_date as session_date1, sd1.drnk as drnk1, sd1.hours_studied as hs1,
           sd1.drnk
           - 
           lag(sd1.drnk) over (partition by sd.student_id, sd.subject order by sd1.session_date) as rank_offset
      from t_session_detail sd
           inner join t_valid_students vs on (vs.student_id = sd.student_id)
           inner join t_session_detail sd1 on (sd1.student_id = sd.student_id and sd1.subject = sd.subject)
),
t_dist_ro as (
    select session_id, student_id, subject, session_date, hours_studied, drnk,
           total_session_length, session_gap, session_date1, drnk1, hs1, rank_offset --,
           --count(distinct rank_offset) over (partition by student_id) as dist_rank_offset  -- Does not work here!
      from t_sessions_cmp
     where rank_offset is null or rank_offset != 0
),
t_distinct_rank_offset as (
    select student_id,
	       count(distinct rank_offset) as cd_ro
	  from t_dist_ro
	 where rank_offset is not null
	 group by student_id
    having count(distinct rank_offset) = 1
),
t_dist_ro1 as (
    select x.session_id, x.student_id, x.subject, x.session_date, x.hours_studied, x.drnk,
           x.total_session_length, x.session_gap, x.session_date1, x.drnk1, x.hs1, x.rank_offset
	  from t_dist_ro x
	 where exists (select null from t_distinct_rank_offset y where y.student_id = x.student_id)
),
t_study_cycle as (
    select student_id,
           count(distinct subject) as cycle_length,
           sum(hs1) as total_study_hours
      from t_dist_ro1
     --where dist_rank_offset = 1
     group by student_id
    having count(distinct subject) >= 3
)
select sc.student_id, s.student_name, s.major, sc.cycle_length, sc.total_study_hours
  from t_study_cycle sc
       inner join students s on (s.student_id = sc.student_id)
 order by sc.cycle_length desc, sc.total_study_hours desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_session_detail as (
    select session_id, student_id, subject, session_date, hours_studied,
           dense_rank() over (partition by student_id order by session_date) as drnk,
           count(*) over (partition by student_id) as total_session_length,
           DATEDIFF(DAY, lag(session_date) over (partition by student_id order by session_date), session_date) as session_gap
      from study_sessions
),
t_valid_students as (
    select distinct ss.student_id
      from study_sessions ss
     where not exists (select null
                         from t_session_detail sd
                        where sd.student_id = ss.student_id
                          and (sd.session_gap > 2 or sd.total_session_length < 6)
                      )
),
t_sessions_cmp as (
    select sd.session_id, sd.student_id, sd.subject, sd.session_date, sd.hours_studied,
           sd.drnk, sd.total_session_length, sd.session_gap,
           sd1.session_date as session_date1, sd1.drnk as drnk1, sd1.hours_studied as hs1,
           sd1.drnk
           - 
           lag(sd1.drnk) over (partition by sd.student_id, sd.subject order by sd1.session_date) as rank_offset
      from t_session_detail sd
           inner join t_valid_students vs on (vs.student_id = sd.student_id)
           inner join t_session_detail sd1 on (sd1.student_id = sd.student_id and sd1.subject = sd.subject)
),
t_dist_ro as (
    select session_id, student_id, subject, session_date, hours_studied, drnk,
           total_session_length, session_gap, session_date1, drnk1, hs1, rank_offset --,
           --count(distinct rank_offset) over (partition by student_id) as dist_rank_offset  -- Does not work here!
      from t_sessions_cmp
     where rank_offset is null or rank_offset != 0
),
t_distinct_rank_offset as (
    select student_id,
	       count(distinct rank_offset) as cd_ro
	  from t_dist_ro
	 where rank_offset is not null
	 group by student_id
    having count(distinct rank_offset) = 1
),
t_dist_ro1 as (
    select x.session_id, x.student_id, x.subject, x.session_date, x.hours_studied, x.drnk,
           x.total_session_length, x.session_gap, x.session_date1, x.drnk1, x.hs1, x.rank_offset
	  from t_dist_ro x
	 where exists (select null from t_distinct_rank_offset y where y.student_id = x.student_id)
),
t_study_cycle as (
    select student_id,
           count(distinct subject) as cycle_length,
           sum(hs1) as total_study_hours
      from t_dist_ro1
     --where dist_rank_offset = 1
     group by student_id
    having count(distinct subject) >= 3
)
select sc.student_id, s.student_name, s.major, sc.cycle_length, sc.total_study_hours
  from t_study_cycle sc
       inner join students s on (s.student_id = sc.student_id)
 order by sc.cycle_length desc, sc.total_study_hours desc
;


# MySQL


# Pandas

