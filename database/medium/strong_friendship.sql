-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
with t (user_id, friend_id) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select f.user1_id, f.user2_id,
       count(*) as common_friend
from friendship f
     inner join t t1 on (t1.user_id = f.user1_id)
     inner join t t2 on (t2.user_id = f.user2_id and t2.friend_id = t1.friend_id)
group by f.user1_id, f.user2_id
having count(*) >= 3
;


# Pandas

