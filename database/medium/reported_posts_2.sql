-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select a.action_date, count(a.post_id) as total_posts
      from (select distinct post_id, action_date, action, extra
              from actions
           ) a
     where a.action = 'report' and a.extra = 'spam'
     group by a.action_date
),
t1 as (
    select x.action_date, count(x.post_id) as removed_posts
      from (
              select distinct a.action_date, r.post_id
                from (select distinct post_id, action_date, action, extra
                        from actions
                     ) a
                     left outer join removals r on (r.post_id = a.post_id)
               where a.action = 'report' and a.extra = 'spam'
           ) x
     group by x.action_date
)
,
t2 as (
    select t.action_date, t1.removed_posts/t.total_posts as removed_ratio
      from t
           inner join t1 on (t.action_date = t1.action_date)
)
select round(avg(removed_ratio)*100, 2) as average_daily_percent
  from t2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select a.action_date, count(a.post_id) as total_posts
      from (select distinct post_id, action_date, action, extra
              from actions
           ) a
     where a.action = 'report' and a.extra = 'spam'
     group by a.action_date
),
t1 as (
    select x.action_date, count(x.post_id) as removed_posts
      from (
              select distinct a.action_date, r.post_id
                from (select distinct post_id, action_date, action, extra
                        from actions
                     ) a
                     left outer join removals r on (r.post_id = a.post_id)
               where a.action = 'report' and a.extra = 'spam'
           ) x
     group by x.action_date
)
,
t2 as (
    select t.action_date, t1.removed_posts::numeric / t.total_posts::numeric as removed_ratio
      from t
           inner join t1 on (t.action_date = t1.action_date)
)
select round(avg(removed_ratio)*100, 2) as average_daily_percent
  from t2
;


# MySQL
# Write your MySQL query statement below
with t as (
    select a.action_date, count(a.post_id) as total_posts
      from (select distinct post_id, action_date, action, extra
              from actions
           ) a
     where a.action = 'report' and a.extra = 'spam'
     group by a.action_date
),
t1 as (
    select x.action_date, count(x.post_id) as removed_posts
      from (
              select distinct a.action_date, r.post_id
                from (select distinct post_id, action_date, action, extra
                        from actions
                     ) a
                     left outer join removals r on (r.post_id = a.post_id)
               where a.action = 'report' and a.extra = 'spam'
           ) x
     group by x.action_date
)
,
t2 as (
    select t.action_date, t1.removed_posts/t.total_posts as removed_ratio
      from t
           inner join t1 on (t.action_date = t1.action_date)
)
select round(avg(removed_ratio)*100, 2) as average_daily_percent
  from t2
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select a.action_date, count(a.post_id) as total_posts
      from (select distinct post_id, action_date, action, extra
              from actions
           ) a
     where a.action = 'report' and a.extra = 'spam'
     group by a.action_date
),
t1 as (
    select x.action_date, count(x.post_id) as removed_posts
      from (
              select distinct a.action_date, r.post_id
                from (select distinct post_id, action_date, action, extra
                        from actions
                     ) a
                     left outer join removals r on (r.post_id = a.post_id)
               where a.action = 'report' and a.extra = 'spam'
           ) x
     group by x.action_date
)
,
t2 as (
    select t.action_date, convert(float, t1.removed_posts) / convert(float, t.total_posts) as removed_ratio
      from t
           inner join t1 on (t.action_date = t1.action_date)
)
select round(avg(removed_ratio)*100, 2) as average_daily_percent
  from t2
;


# Pandas
import pandas as pd

def reported_posts(actions: pd.DataFrame, removals: pd.DataFrame) -> pd.DataFrame:
    df = ( actions[['post_id','action_date','action','extra']]
          .drop_duplicates()
          .query("action=='report' and extra=='spam'")
         )
    df1 = ( df
           .groupby('action_date',as_index=0)['post_id']
           .count()
           .rename(columns={'post_id':'total_posts'})
          )
    df2 = ( df
           .merge(removals, how='left', on='post_id')
           .groupby('action_date',as_index=0)['remove_date']
           .count()
           .rename(columns={'remove_date':'removed_posts'})
          )
    df3 = df1.merge(df2, how='left', on='action_date')
    df3['average_daily_percent'] = df3['removed_posts']/df3['total_posts']
    return pd.DataFrame(data={'average_daily_percent': round(df3['average_daily_percent'].mean()*100, 2)}, index=[0])

