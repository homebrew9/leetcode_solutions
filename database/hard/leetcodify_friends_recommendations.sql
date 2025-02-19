-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select a.user_id as user1_id,
           b.user_id as user2_id,
           a.day,
           count(distinct a.song_id) as song_count
      from listens a
           inner join listens b on (b.song_id = a.song_id and b.day = a.day and a.user_id != b.user_id)
     group by a.user_id, b.user_id, a.day
   having count(distinct a.song_id) >= 3
),
friends (user1_id, user2_id) as (
    select user1_id, user2_id from friendship
    union all
    select user2_id, user1_id from friendship
)
select distinct t.user1_id as user_id, t.user2_id as recommended_id
  from t
 where not exists (select null from friends f1 where f1.user1_id = t.user1_id and f1.user2_id = t.user2_id)
   and not exists (select null from friends f2 where f2.user2_id = t.user1_id and f2.user1_id = t.user2_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select a.user_id as user1_id,
           b.user_id as user2_id,
           a.day,
           count(distinct a.song_id) as song_count
      from listens a
           inner join listens b on (b.song_id = a.song_id and b.day = a.day and a.user_id != b.user_id)
     group by a.user_id, b.user_id, a.day
    having count(distinct a.song_id) >= 3
),
friends (user1_id, user2_id) as (
    select user1_id, user2_id from friendship
    union all
    select user2_id, user1_id from friendship
)
select distinct t.user1_id as user_id, t.user2_id as recommended_id
  from t
 where not exists (select null from friends f1 where f1.user1_id = t.user1_id and f1.user2_id = t.user2_id)
   and not exists (select null from friends f2 where f2.user2_id = t.user1_id and f2.user1_id = t.user2_id)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select a.user_id as user1_id,
           b.user_id as user2_id,
           a.day,
           count(distinct a.song_id) as song_count
      from listens a
           inner join listens b on (b.song_id = a.song_id and b.day = a.day and a.user_id != b.user_id)
     group by a.user_id, b.user_id, a.day
    having count(distinct a.song_id) >= 3
),
friends (user1_id, user2_id) as (
    select user1_id, user2_id from friendship
    union all
    select user2_id, user1_id from friendship
)
select distinct t.user1_id as user_id, t.user2_id as recommended_id
  from t
 where not exists (select null from friends f1 where f1.user1_id = t.user1_id and f1.user2_id = t.user2_id)
   and not exists (select null from friends f2 where f2.user2_id = t.user1_id and f2.user1_id = t.user2_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select a.user_id as user1_id,
           b.user_id as user2_id,
           a.day,
           count(distinct a.song_id) as song_count
      from listens a
           inner join listens b on (b.song_id = a.song_id and b.day = a.day and a.user_id != b.user_id)
     group by a.user_id, b.user_id, a.day
    having count(distinct a.song_id) >= 3
),
friends (user1_id, user2_id) as (
    select user1_id, user2_id from friendship
    union all
    select user2_id, user1_id from friendship
)
select distinct t.user1_id as user_id, t.user2_id as recommended_id
  from t
       left outer join friends f1 on (f1.user1_id = t.user1_id and f1.user2_id = t.user2_id)
       left outer join friends f2 on (f2.user2_id = t.user1_id and f2.user1_id = t.user2_id)
 where f1.user1_id is null
   and f2.user2_id is null
;

