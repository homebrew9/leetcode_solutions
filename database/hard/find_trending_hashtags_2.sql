-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select regexp_substr(tweet, '#[^# ]+', 1, iter.pos) as hashtag
      from tweets
           cross join ( select level as pos
                          from dual
                       connect by level <= (select max(length(tweet)) from tweets)
                      ) iter
     where regexp_substr(tweet, '#[^# ]+', 1, iter.pos) is not null
),
t1 as (
    select hashtag, count(*) as count
      from t
     group by hashtag
     order by count(*) desc, hashtag desc
)
select hashtag, count
  from t1
 where rownum <= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select regexp_split_to_table(tweet, '\s+') as hashtag
      from tweets
)
select hashtag, count(*) as count
  from t
 where hashtag like '#%'
 group by hashtag
 order by count(*) desc, hashtag desc
 limit 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with iter (pos, lim) as (
    select 1, max(len(tweet))
      from tweets
    union all
    select pos + 1, lim
      from iter
     where pos + 1 <= lim
),
t as (
    select distinct tweet_id, tweet, charindex('#', tweet, iter.pos) as idx
      from tweets
           cross join iter
    where charindex('#', tweet, iter.pos) > 0
),
t1 as (
    select tweet, idx, charindex(' ', tweet, idx+1) as idx2,
           case when charindex(' ', tweet, idx+1) = 0
                then substring(tweet, idx, len(tweet))
                else substring(tweet, idx, charindex(' ', tweet, idx+1) - idx)
           end as hashtag
      from t
)
select top 3 hashtag, count(*) as count
  from t1
 group by hashtag
 order by count(*) desc, hashtag desc
;


# MySQL
# Write your MySQL query statement below
with recursive t (max_len) as (
    select max(length(tweet))
      from tweets
),
t_hier (pos) as (
    select 1
    union all
    select pos + 1
      from t_hier
     where pos + 1 <= (select max_len from t)
),
t1 as (
    select regexp_substr(tweet, '#[^# ]+', 1, t_hier.pos) as hashtag
      from tweets
           cross join t_hier
     where regexp_substr(tweet, '#[^# ]+', 1, t_hier.pos) is not null
)
select hashtag, count(*) as count
  from t1
 group by hashtag
 order by count(*) desc, hashtag desc
 limit 3
;


# Pandas
import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extractall.html
    # Capture group names are used for column names of the result of extractall
    df = ( tweets['tweet']
          .str
          .extractall(r'(?P<hashtag>#[^# ]+)')
          .reset_index()
         )
    return ( df
            .groupby('hashtag', as_index=0)['match']
            .count()
            .rename(columns={'match': 'count'})
            .sort_values(by=['count', 'hashtag'], ascending=[0, 0])
            .head(3)
           )

