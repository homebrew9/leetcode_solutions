-- Oracle
/* Write your PL/SQL query statement below */
select tweet_id
from Tweets
where length(content) > 15
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select tweet_id
from Tweets
where length(content) > 15
;


-- SQL Server
/* Write your T-SQL query statement below */
select tweet_id
from Tweets
where len(content) > 15
;


# MySQL
# Write your MySQL query statement below
select tweet_id
from Tweets
where length(content) > 15
;


# Pandas
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
    
