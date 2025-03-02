-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select distinct p.post_id, k.topic_id
from posts p
     cross join keywords k
where regexp_like(lower(p.content), '(^|\W)'||lower(k.word)||'(\W|$)')
)
select post_id, listagg(topic_id, ',') within group (order by topic_id) as topic
from t
group by post_id
union all
select post_id, 'Ambiguous!'
from posts
where post_id not in (select distinct post_id from t)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select distinct p.post_id, k.topic_id
from posts p
     cross join keywords k
where regexp_like(lower(p.content), '(^|\W)'||lower(k.word)||'(\W|$)')
)
select post_id, string_agg(topic_id::text, ',' order by topic_id) as topic
from t
group by post_id
union all
select post_id, 'Ambiguous!'
from posts
where post_id not in (select distinct post_id from t)
;


# MySQL
# Write your MySQL query statement below
with t as (
select distinct p.post_id, k.topic_id
from posts p
     cross join keywords k
where regexp_like( lower(p.content),
                   concat('(^|[^a-zA-Z_]+)' , lower(k.word) , '([^a-zA-Z_]+|$)')
                 )
)
select post_id, group_concat(topic_id order by topic_id separator ',') as topic
from t
group by post_id
union all
select post_id, 'Ambiguous!'
from posts
where post_id not in (select distinct post_id from t)
;

