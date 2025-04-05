-- Oracle
/* Write your PL/SQL query statement below */
with t (voter, candidate, votes) as (
select voter, candidate,
       1 / count(*) over (partition by voter) as votes
from votes
),
t1 (candidate, total_votes) as (
select candidate, sum(votes) as total_votes
from t
where candidate is not null
group by candidate
)
select x.candidate
from t1 x
where x.total_votes = (select max(total_votes) from t1)
order by x.candidate
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (voter, candidate, votes) as (
select voter, candidate,
       1::numeric / count(*) over (partition by voter)::numeric as votes
from votes
),
t1 (candidate, total_votes) as (
select candidate, sum(votes) as total_votes
from t
where candidate is not null
group by candidate
)
select x.candidate
from t1 x
where x.total_votes = (select max(total_votes) from t1)
order by x.candidate
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (voter, candidate, votes) as (
select voter, candidate,
       1.0 / CONVERT(FLOAT, count(*) over (partition by voter)) as votes
from votes
),
t1 (candidate, total_votes) as (
select candidate, sum(votes) as total_votes
from t
where candidate is not null
group by candidate
)
select x.candidate
from t1 x
where x.total_votes = (select max(total_votes) from t1)
order by x.candidate
;


# MySQL
# Write your MySQL query statement below
with t (voter, candidate, votes) as (
select voter, candidate,
       1 / count(*) over (partition by voter) as votes
from votes
),
t1 (candidate, total_votes) as (
select candidate, sum(votes) as total_votes
from t
where candidate is not null
group by candidate
)
select x.candidate
from t1 x
where x.total_votes = (select max(total_votes) from t1)
order by x.candidate
;


# Pandas
import pandas as pd

def get_election_results(votes: pd.DataFrame) -> pd.DataFrame:
    df = votes.groupby('voter', as_index=False).count().rename(columns={'candidate': 'vote_count'})
    df1 = votes.merge(df, how='inner', on='voter')
    df1['vote_count'] = np.where(df1['vote_count'] != 0, 1/df1['vote_count'], 0)
    df2 = df1.groupby('candidate', as_index=False)['vote_count'].sum()
    max_vote_count = max(df2['vote_count'])
    return df2[df2['vote_count'] == max_vote_count][['candidate']].sort_values('candidate')

