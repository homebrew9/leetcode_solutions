-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select regexp_substr(tweet, '#\S+') as hashtag, count(*) as hashtag_count
      from tweets
     group by regexp_substr(tweet, '#\S+')
     order by hashtag_count desc, hashtag desc
)
select hashtag, hashtag_count
  from t
 where rownum <= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select regexp_replace(tweet, '^.*(#\S+).*$', '\1') as hashtag, count(*) as hashtag_count
      from tweets
     group by regexp_replace(tweet, '^.*(#\S+).*$', '\1')
     order by hashtag_count desc, hashtag desc
)
select hashtag, hashtag_count
  from t
 limit 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (hashtag) as (
    select case when charindex(' ', tweet, charindex('#', tweet)) = 0
                then substring(tweet, charindex('#', tweet), len(tweet))
                else substring(tweet,
                               charindex('#', tweet),
                               charindex(' ', tweet, charindex('#', tweet)) - charindex('#', tweet)
                              )
           end as hashtag
      from tweets
)
select top 3 hashtag, count(*) as hashtag_count
  from t
 group by hashtag
 order by hashtag_count desc, hashtag desc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select regexp_substr(tweet, '#[A-Za-z]+') as hashtag, count(*) as hashtag_count
      from tweets
     group by regexp_substr(tweet, '#[A-Za-z]+')
     order by hashtag_count desc, hashtag desc
)
select hashtag, hashtag_count
  from t
 limit 3
;


# Pandas
import pandas as pd

def find_trending_hashtags(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['hashtag'] = tweets['tweet'].str.replace(r'^.*(#\S+).*$', r'\1', regex=True)
    return ( tweets[['tweet_id','hashtag']]
            .groupby('hashtag', as_index=0)['tweet_id']
            .count()
            .rename(columns={'tweet_id':'hashtag_count'})
            .sort_values(by=['hashtag_count','hashtag'], ascending=[0,0])
            .head(3)
           )

