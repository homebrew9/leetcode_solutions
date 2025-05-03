-- Oracle
/* Write your PL/SQL query statement below */
select tweet_id
from Tweets
where length(content) > 140
or regexp_count(content, '@') > 3
or regexp_count(content, '#') > 3
order by tweet_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select tweet_id
from Tweets
where length(content) > 140
or regexp_count(content, '@') > 3
or regexp_count(content, '#') > 3
order by tweet_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select tweet_id
from Tweets
where len(content) > 140
or len(content) - len(replace(content, '@', '')) > 3
or len(content) - len(replace(content, '#', '')) > 3
order by tweet_id
;


# MySQL
# Write your MySQL query statement below
select tweet_id
from Tweets
where length(content) > 140
or length(content) - length(replace(content, '@', '')) > 3
or length(content) - length(replace(content, '#', '')) > 3
order by tweet_id
;


# Pandas
import pandas as pd

def find_invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return ( tweets[ (tweets.content.str.len() > 140) |
                     (tweets.content.str.count('@') > 3) |
                     (tweets.content.str.count('#') > 3)
                   ][['tweet_id']]
            .sort_values('tweet_id')
           )

