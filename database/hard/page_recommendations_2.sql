-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, friend_id) as (
select user1_id as user_id, user2_id as friend_id
from friendship
union all
select user2_id, user1_id
from friendship
)
select t.user_id,
       a.page_id as page_id,
       count(distinct t.friend_id) as friends_likes
from t
     inner join likes a on (a.user_id = t.friend_id)
where not exists (
    select null
    from likes b
    where b.user_id = t.user_id
    and b.page_id = a.page_id
)
group by t.user_id, a.page_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, friend_id) as (
select user1_id as user_id, user2_id as friend_id
from friendship
union all
select user2_id, user1_id
from friendship
)
select t.user_id,
       a.page_id as page_id,
       count(distinct t.friend_id) as friends_likes
from t
     inner join likes a on (a.user_id = t.friend_id)
where not exists (
    select null
    from likes b
    where b.user_id = t.user_id
    and b.page_id = a.page_id
)
group by t.user_id, a.page_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, friend_id) as (
select user1_id as user_id, user2_id as friend_id
from friendship
union all
select user2_id, user1_id
from friendship
)
select t.user_id,
       a.page_id as page_id,
       count(distinct t.friend_id) as friends_likes
from t
     inner join likes a on (a.user_id = t.friend_id)
where not exists (
    select null
    from likes b
    where b.user_id = t.user_id
    and b.page_id = a.page_id
)
group by t.user_id, a.page_id
;


# MySQL
# Write your MySQL query statement below
with t (user_id, friend_id) as (
select user1_id as user_id, user2_id as friend_id
from friendship
union all
select user2_id, user1_id
from friendship
)
select t.user_id,
       a.page_id as page_id,
       count(distinct t.friend_id) as friends_likes
from t
     inner join likes a on (a.user_id = t.friend_id)
where not exists (
    select null
    from likes b
    where b.user_id = t.user_id
    and b.page_id = a.page_id
)
group by t.user_id, a.page_id
;

