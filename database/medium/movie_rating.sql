-- Oracle
/* Write your PL/SQL query statement below */
--
WITH t (title, name, rating, created_at, movie_count, movie_rating) AS (
SELECT m.title, u.name, mr.rating, mr.created_at,
       count(*) OVER (PARTITION BY u.name) AS movie_count,
       avg(CASE WHEN trunc(created_at,'MM') = DATE'2020-02-01' THEN rating END) OVER (PARTITION BY m.title) AS movie_rating
FROM MovieRating mr
     INNER JOIN Movies m ON (m.movie_id = mr.movie_id)
     INNER JOIN Users u ON (u.user_id = mr.user_id)
),
t1 (title, name, rating, created_at, movie_count, movie_rating, drnk1, drnk2) AS (
SELECT title, name, rating, created_at, movie_count, movie_rating,
       dense_rank() OVER (ORDER BY movie_count DESC, name) AS drnk1,
       dense_rank() OVER (ORDER BY nvl(movie_rating, 0) DESC, title) AS drnk2
FROM t
)
SELECT DISTINCT name as results FROM t1 WHERE drnk1 = 1 UNION ALL
SELECT DISTINCT title FROM t1 WHERE drnk2 = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select user_id, count(*) as cnt
    from movierating
    group by user_id
),
t1 as (
    select u.name, cnt
    from t
         inner join users u on (u.user_id = t.user_id)
    order by cnt desc, u.name
),
t2 as (
    select name as results
    from t1
    limit 1
),
t3 as (
    select movie_id, avg(rating) as avg_rating
    from movierating
    where to_char(created_at, 'yyyymm') = '202002'
    group by movie_id
),
t4 as (
    select m.title, avg_rating
    from t3
         inner join movies m on (m.movie_id = t3.movie_id)
    order by avg_rating desc, m.title
),
t5 as (
    select title as results
    from t4
    limit 1
)
select results from t2 union all
select results from t5
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, count(*) as cnt
    from movierating
    group by user_id
),
t1 as (
    select t.user_id, t.cnt, u.name,
           dense_rank() over (order by cnt desc, u.name) as drnk
    from t
         inner join users u on (u.user_id = t.user_id)
),
t3 as (
    select movie_id, avg(convert(float, rating)) as avg_rating
    from movierating
    where year(created_at) = 2020 and month(created_at) = 2
    group by movie_id
),
t4 as (
    select t3.movie_id, t3.avg_rating, m.title,
           dense_rank() over (order by t3.avg_rating desc, m.title) as drnk
    from t3
         inner join movies m on (m.movie_id = t3.movie_id)
)
select t1.name as results from t1 where t1.drnk = 1
union all
select t4.title from t4 where t4.drnk = 1
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, count(*) as cnt
    from movierating
    group by user_id
),
t1 as (
    select t.user_id, t.cnt, u.name,
           dense_rank() over (order by cnt desc, u.name) as drnk
    from t
         inner join users u on (u.user_id = t.user_id)
),
t3 as (
    select movie_id, avg(rating) as avg_rating
    from movierating
    where year(created_at) = 2020 and month(created_at) = 2
    group by movie_id
),
t4 as (
    select t3.movie_id, t3.avg_rating, m.title,
           dense_rank() over (order by t3.avg_rating desc, m.title) as drnk
    from t3
         inner join movies m on (m.movie_id = t3.movie_id)
)
select t1.name as results from t1 where t1.drnk = 1
union all
select t4.title from t4 where t4.drnk = 1
;


# Pandas
import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    df = ( movie_rating
          .merge(users, how='inner', on='user_id')
          .groupby(['user_id','name'], as_index=0)['movie_id']
          .count()
          .sort_values(by=['movie_id', 'name'], ascending=[0, 1])
          .head(1)[['name']]
          .rename(columns={'name': 'results'})
         )
    df1 = ( movie_rating[movie_rating['created_at'].dt.strftime('%Y%m') == '202002']
           .merge(movies, how='inner', on='movie_id')
           .groupby(['movie_id','title'], as_index=0)['rating']
           .mean()
           .sort_values(by=['rating', 'title'], ascending=[0, 1])
           .head(1)[['title']]
           .rename(columns={'title': 'results'})
          )
    return pd.concat([df, df1])

