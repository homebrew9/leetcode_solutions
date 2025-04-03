-- Oracle
/* Write your PL/SQL query statement below */
with t (id) as (
    select x.requester_id from RequestAccepted x union all
    select y.accepter_id from RequestAccepted y
),
t1 (id, num) as (
    select id, count(*) as num
      from t
     group by id
),
t2 (id, num, drnk) as (
    select id, num, dense_rank() over (order by num desc) as drnk
      from t1
)
select id, num
from t2
where drnk = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (person_id, friend_id) as (
    select x.person_id, x.friend_id
      from (
          select requester_id as person_id, accepter_id as friend_id from requestaccepted
          union all
          select accepter_id, requester_id from requestaccepted
      ) x
),
t1 as (
    select person_id, count(friend_id) as friend_count
      from t
     group by person_id
)
select person_id as id, friend_count as num
  from t1
 where friend_count = (select max(friend_count) from t1)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (person_id, friend_id) as (
    select x.person_id, x.friend_id
      from (
          select requester_id as person_id, accepter_id as friend_id from requestaccepted
          union all
          select accepter_id, requester_id from requestaccepted
      ) x
),
t1 as (
    select person_id, count(friend_id) as friend_count
      from t
     group by person_id
)
select person_id as id, friend_count as num
  from t1
 where friend_count = (select max(friend_count) from t1)
;


# MySQL
# Write your MySQL query statement below
with t (person_id, friend_id) as (
    select x.person_id, x.friend_id
      from (
          select requester_id as person_id, accepter_id as friend_id from requestaccepted
          union all
          select accepter_id, requester_id from requestaccepted
      ) x
),
t1 as (
    select person_id, count(friend_id) as friend_count
      from t
     group by person_id
)
select person_id as id, friend_count as num
  from t1
 where friend_count = (select max(friend_count) from t1)
;


# Pandas
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    df = ( pd.concat([
             request_accepted[['requester_id','accepter_id']].rename(columns={'requester_id':'id', 'accepter_id':'num'}),
             request_accepted[['accepter_id','requester_id']].rename(columns={'accepter_id':'id', 'requester_id':'num'})]
           )
         )
    df1 = df.groupby('id',as_index=0)['num'].count()
    return df1[df1['num'] == df1['num'].max()]

