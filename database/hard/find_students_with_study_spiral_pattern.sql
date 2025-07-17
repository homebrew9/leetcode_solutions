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
           total_session_length, session_gap, session_date1, drnk1, hs1, rank_offset #,
           #count(distinct rank_offset) over (partition by student_id) as dist_rank_offset  # Does not work here!
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
     #where dist_rank_offset = 1
     group by student_id
    having count(distinct subject) >= 3
)
select sc.student_id, s.student_name, s.major, sc.cycle_length, sc.total_study_hours
  from t_study_cycle sc
       inner join students s on (s.student_id = sc.student_id)
 order by sc.cycle_length desc, sc.total_study_hours desc
;


# Pandas
import pandas as pd

def find_study_spiral_pattern(students: pd.DataFrame, study_sessions: pd.DataFrame) -> pd.DataFrame:
    # 1) Generate dense ranks (drnk) per student ordered by session date
    # 2) Determine student_ids with total study length < 6 and session date diff > 2 days and remove them
    # 3) Merge df with itself on student and subject and find rank_offset = diff of curr and previous drnk
    # 4) Remove all rank_offsets that are NaN or 0. In this dataset, find all invalid student_ids who
    #    have distinct subjects < 3 or distinct rank_offset != 1. Remove these student_ids.
    # 5) Now we have the final clean dataset. Find distinct tuples (student_id, session_date, subject, hours_studied)
    #    and calculate the required aggregations.
    study_sessions.session_date = pd.to_datetime(study_sessions.session_date)
    study_sessions.sort_values(['student_id','session_date'], inplace=True)
    study_sessions['drnk'] = ( study_sessions
                              .groupby('student_id', as_index=0)['session_date']
                              .rank(method='dense')
                             )
    invalid_student_ids1 = ( study_sessions
                            .groupby('student_id', as_index=0)
                            .size()
                            .query('size < 6')['student_id']
                           )
    invalid_student_ids2 = ( study_sessions
                            .merge(study_sessions, how='inner', on='student_id')
                            .query('drnk_y == drnk_x + 1 and (session_date_y - session_date_x).dt.days > 2')['student_id']
                           )
    df = ( study_sessions[ (~study_sessions['student_id'].isin(invalid_student_ids1))
                           &
                           (~study_sessions['student_id'].isin(invalid_student_ids2))
                         ]
         )
    df1 = ( df
           .merge(df, how='inner', on=['student_id','subject'])
           .sort_values(['student_id','session_date_x','session_date_y'])
          )
    df1['prev_drnk'] = ( df1
                        .groupby(['student_id','session_date_x'], as_index=0)['drnk_y']
                        .shift(1)
                       )
    df1['rank_offset'] = df1['drnk_y'] - df1['prev_drnk']
    df2 = df1.query('~rank_offset.isna() and rank_offset != 0') 
    invalid_student_ids3 = ( df2
                            .groupby('student_id', as_index=0)
                            .agg(dist_rank_offsets=('rank_offset', 'nunique'))
                            .query('dist_rank_offsets != 1')['student_id']
                           )
    invalid_student_ids4 = ( df2
                            .groupby('student_id', as_index=0)
                            .agg(dist_subjects=('subject', 'nunique'))
                            .query('dist_subjects < 3')['student_id']
                           )
    df3 = ( df2[ (~df2['student_id'].isin(invalid_student_ids3))
                 &
                 (~df2['student_id'].isin(invalid_student_ids4))
               ]
           .sort_values(['student_id','session_date_x','subject','hours_studied_x'])[['student_id','subject','session_date_x','hours_studied_x']]
           .drop_duplicates()
           .groupby('student_id', as_index=0)
           .agg(cycle_length=('subject', 'nunique'), total_study_hours=('hours_studied_x', 'sum'))
          )
    return students.merge(df3, how='inner', on='student_id').sort_values(by=['cycle_length','total_study_hours'], ascending=[0,0])











