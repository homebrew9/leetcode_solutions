-- Oracle
/* Write your PL/SQL query statement below */
select distinct f.user1_id, f.user2_id --, a.day, count(distinct a.song_id) as song_count
from friendship f
     inner join listens a on (a.user_id = f.user1_id)
     inner join listens b on (b.user_id = f.user2_id and b.song_id = a.song_id and b.day = a.day)
group by f.user1_id, f.user2_id, a.day
having count(distinct a.song_id) >= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct f.user1_id, f.user2_id --, a.day, count(distinct a.song_id) as song_count
from friendship f
     inner join listens a on (a.user_id = f.user1_id)
     inner join listens b on (b.user_id = f.user2_id and b.song_id = a.song_id and b.day = a.day)
group by f.user1_id, f.user2_id, a.day
having count(distinct a.song_id) >= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct f.user1_id, f.user2_id --, a.day, count(distinct a.song_id) as song_count
from friendship f
     inner join listens a on (a.user_id = f.user1_id)
     inner join listens b on (b.user_id = f.user2_id and b.song_id = a.song_id and b.day = a.day)
group by f.user1_id, f.user2_id, a.day
having count(distinct a.song_id) >= 3
;


# MySQL
# Write your MySQL query statement below
select distinct f.user1_id, f.user2_id
       #, a.day, count(distinct a.song_id) as song_count
from friendship f
     inner join listens a on (a.user_id = f.user1_id)
     inner join listens b on (b.user_id = f.user2_id and b.song_id = a.song_id and b.day = a.day)
group by f.user1_id, f.user2_id, a.day
having count(distinct a.song_id) >= 3
;

