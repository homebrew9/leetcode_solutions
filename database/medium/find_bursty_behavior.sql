-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, avg_weekly_posts) as (
    select user_id, count(*) / 4
      from posts
     where trunc(post_date) between DATE'2024-02-01' and DATE'2024-02-28'
    group by user_id
),
t1 (user_id, post_id, cnt) as (
    select p1.user_id, p1.post_id, count(*) as cnt
      from posts p1
           inner join posts p2 on (p2.user_id = p1.user_id and
                                   trunc(p2.post_date) between DATE'2024-02-01' and DATE'2024-02-28' and
                                   trunc(p2.post_date) between trunc(p1.post_date) and trunc(p1.post_date + 6)
                                  )
     where trunc(p1.post_date) between DATE'2024-02-01'  and DATE'2024-02-28'
     group by p1.user_id, p1.post_id
),
t2 (user_id, max_7day_posts) as (
    select user_id, max(cnt) as max_7day_posts
      from t1
     group by user_id
)
select t.user_id, t2.max_7day_posts, t.avg_weekly_posts
  from t
       inner join t2 on (t2.user_id = t.user_id and t2.max_7day_posts >= 2 * t.avg_weekly_posts)
 order by t.user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, avg_weekly_posts) as (
    select user_id, count(*)::numeric / 4
      from posts
     where post_date::date between '2024-02-01' and '2024-02-28'
    group by user_id
),
t1 (user_id, post_date, cnt) as (
    select p1.user_id, p1.post_date,
           (select count(*)
              from posts p2
             where p2.user_id = p1.user_id
               and p2.post_date::date between '2024-02-01' and '2024-02-28'
               and p2.post_date::date between p1.post_date::date and (p1.post_date::date + interval '6 day')
           ) as cnt
      from posts p1
     where p1.post_date::date between '2024-02-01' and '2024-02-28'
),
t2 (user_id, max_7day_posts) as (
    select user_id, max(cnt) as max_7day_posts
      from t1
     group by user_id
)
select t.user_id, t2.max_7day_posts, t.avg_weekly_posts
  from t
       inner join t2 on (t2.user_id = t.user_id and t2.max_7day_posts >= 2 * t.avg_weekly_posts)
 order by t.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, avg_weekly_posts) as (
    select user_id, convert(float, count(*)) / 4
      from posts
     where post_date between '2024-02-01' and '2024-02-28'
    group by user_id
)
,
t1 (user_id, post_date, cnt) as (
    select p1.user_id, p1.post_date,
           (select count(*)
              from posts p2
             where p2.user_id = p1.user_id
               and p2.post_date between '2024-02-01' and '2024-02-28'
               and p2.post_date between p1.post_date and dateadd(day, 6, p1.post_date)
           ) as cnt
      from posts p1
     where p1.post_date between '2024-02-01' and '2024-02-28'
),
t2 (user_id, max_7day_posts) as (
    select user_id, max(cnt) as max_7day_posts
      from t1
     group by user_id
)
select t.user_id, t2.max_7day_posts, t.avg_weekly_posts
  from t
       inner join t2 on (t2.user_id = t.user_id and t2.max_7day_posts >= 2 * t.avg_weekly_posts)
 order by t.user_id
;


# MySQL
# Write your MySQL query statement below
with t (user_id, avg_weekly_posts) as (
    select user_id, count(*) / 4
      from posts
     where post_date between '2024-02-01' and '2024-02-28'
    group by user_id
),
t1 (user_id, post_date, cnt) as (
    select p1.user_id, p1.post_date,
           (select count(*)
              from posts p2
             where p2.user_id = p1.user_id
               and p2.post_date between '2024-02-01' and '2024-02-28'
               and p2.post_date between p1.post_date and (p1.post_date + interval 6 day)
           ) as cnt
      from posts p1
     where p1.post_date between '2024-02-01' and '2024-02-28'
),
t2 (user_id, max_7day_posts) as (
    select user_id, max(cnt) as max_7day_posts
      from t1
     group by user_id
)
select t.user_id, t2.max_7day_posts, t.avg_weekly_posts
  from t
       inner join t2 on (t2.user_id = t.user_id and
                         t2.max_7day_posts >= 2 * t.avg_weekly_posts
                        )
 order by t.user_id
;


# Pandas
import pandas as pd

def find_bursty_behavior(posts: pd.DataFrame) -> pd.DataFrame:
    posts = posts.query('post_date >= "2024-02-01" and post_date <= "2024-02-28"')
    df = ( posts
          .groupby('user_id',as_index=0)['post_id']
          .count()
          .rename(columns={'post_id': 'avg_weekly_posts'})
         )
    df['avg_weekly_posts'] = df['avg_weekly_posts']/4
    posts['post_date_plus7'] = posts['post_date'] + pd.DateOffset(days=6)
    df1 = ( posts
           .merge(posts, how='inner', on='user_id')
           .query('post_date_y >= post_date_x and post_date_y <= post_date_plus7_x')
           .groupby(['user_id','post_id_x'], as_index=0)['post_id_y']
           .count()
           .rename(columns={'post_id_y': 'cnt'})
          )
    df1 = ( df1
           .groupby('user_id',as_index=0)['cnt']
           .max()
           .rename(columns={'cnt': 'max_7day_posts'})
          )
    return ( df1
            .merge(df, how='inner', on='user_id')
            .query('max_7day_posts >= 2 * avg_weekly_posts')
            .sort_values('user_id')
           )

