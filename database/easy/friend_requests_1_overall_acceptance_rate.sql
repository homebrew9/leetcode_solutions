-- Oracle
/* Write your PL/SQL query statement below */
with friendrequest_dist (sender_id, send_to_id, request_date) as (
    select sender_id, send_to_id, request_date
      from (select sender_id, send_to_id, request_date,
               row_number() over (partition by sender_id, send_to_id order by request_date) as rnum
          from FriendRequest) x
     where x.rnum = 1
),
requestaccepted_dist (requester_id, accepter_id, accept_date) as (
    select requester_id, accepter_id, accept_date
      from (select requester_id, accepter_id, accept_date,
               row_number() over (partition by requester_id, accepter_id order by accept_date) as rnum
          from RequestAccepted) x
     where x.rnum = 1
),
t1 (total_requests_sent) as (
    select count(*) from friendrequest_dist
),
t2 (total_requests_accepted) as (
    select count(*) from requestaccepted_dist
)
select case when t1.total_requests_sent = 0 then 0.00
            else round(t2.total_requests_accepted / t1.total_requests_sent, 2)
       end as "accept_rate"
  from t1 cross join t2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with friendrequest_dist (sender_id, send_to_id, request_date) as (
    select sender_id, send_to_id, request_date
      from (select sender_id, send_to_id, request_date,
               row_number() over (partition by sender_id, send_to_id order by request_date) as rnum
          from FriendRequest) x
     where x.rnum = 1
),
requestaccepted_dist (requester_id, accepter_id, accept_date) as (
    select requester_id, accepter_id, accept_date
      from (select requester_id, accepter_id, accept_date,
               row_number() over (partition by requester_id, accepter_id order by accept_date) as rnum
          from RequestAccepted) x
     where x.rnum = 1
),
t1 (total_requests_sent) as (
    select count(*) from friendrequest_dist
),
t2 (total_requests_accepted) as (
    select count(*) from requestaccepted_dist
)
select case when t1.total_requests_sent = 0 then 0.00
            else round(cast(t2.total_requests_accepted::float / t1.total_requests_sent::float as numeric), 2)
       end as accept_rate
  from t1 cross join t2
;


-- SQL Server
/* Write your T-SQL query statement below */
with friendrequest_dist (sender_id, send_to_id, request_date) as (
    select sender_id, send_to_id, request_date
      from (select sender_id, send_to_id, request_date,
               row_number() over (partition by sender_id, send_to_id order by request_date) as rnum
          from FriendRequest) x
     where x.rnum = 1
),
requestaccepted_dist (requester_id, accepter_id, accept_date) as (
    select requester_id, accepter_id, accept_date
      from (select requester_id, accepter_id, accept_date,
               row_number() over (partition by requester_id, accepter_id order by accept_date) as rnum
          from RequestAccepted) x
     where x.rnum = 1
),
t1 (total_requests_sent) as (
    select count(*) from friendrequest_dist
),
t2 (total_requests_accepted) as (
    select count(*) from requestaccepted_dist
)
select case when t1.total_requests_sent = 0 then 0.00
            else round(convert(float, t2.total_requests_accepted) / convert(float, t1.total_requests_sent), 2)
       end as "accept_rate"
  from t1 cross join t2
;


# MySQL
# Write your MySQL query statement below
with friendrequest_dist (sender_id, send_to_id, request_date) as (
    select sender_id, send_to_id, request_date
      from (select sender_id, send_to_id, request_date,
               row_number() over (partition by sender_id, send_to_id order by request_date) as rnum
          from FriendRequest) x
     where x.rnum = 1
),
requestaccepted_dist (requester_id, accepter_id, accept_date) as (
    select requester_id, accepter_id, accept_date
      from (select requester_id, accepter_id, accept_date,
               row_number() over (partition by requester_id, accepter_id order by accept_date) as rnum
          from RequestAccepted) x
     where x.rnum = 1
),
t1 (total_requests_sent) as (
    select count(*) from friendrequest_dist
),
t2 (total_requests_accepted) as (
    select count(*) from requestaccepted_dist
)
select case when t1.total_requests_sent = 0 then 0.00
            else round(t2.total_requests_accepted / t1.total_requests_sent, 2)
       end as "accept_rate"
  from t1 cross join t2
;


# Pandas
import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    friend_request['rnum'] = friend_request.groupby(['sender_id','send_to_id'])['request_date'].rank(method='first')
    request_accepted['rnum'] = request_accepted.groupby(['requester_id','accepter_id'])['accept_date'].rank(method='first')
    requests_sent = len(friend_request[friend_request['rnum']==1])
    requests_accepted = len(request_accepted[request_accepted['rnum']==1])
    val = 0 if requests_sent == 0 else round(requests_accepted/requests_sent, 2)
    return pd.DataFrame(data=[val], columns=['accept_rate'])

