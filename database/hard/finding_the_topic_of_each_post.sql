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


-- SQL Server
/* Write your T-SQL query statement below */
with t (post_id, topic_id) as (
    select distinct p.post_id, k.topic_id
    from posts p
        cross apply string_split(p.content, ' ') ss
        inner join keywords k on (lower(k.word) = lower(ss.value))
)
select post_id, string_agg(topic_id, ',') within group (order by topic_id) as topic
  from t
 group by post_id
union all
select p.post_id, 'Ambiguous!' as topic
  from posts p
 where not exists (select null from t where t.post_id = p.post_id)
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


# Pandas
import pandas as pd

def find_topic(keywords: pd.DataFrame, posts: pd.DataFrame) -> pd.DataFrame:
    keywords['word_lower'] = keywords['word'].str.lower()
    posts['content'] = posts['content'].str.split(' ')
    df = posts.explode('content')
    df['content_lower'] = df['content'].str.lower()
    df1 = ( df
           .merge(keywords, how='inner', left_on='content_lower', right_on='word_lower')[['post_id','topic_id']]
           .drop_duplicates()
           .sort_values(['post_id','topic_id'])
           .groupby('post_id', as_index=0)['topic_id']
           .apply(lambda x: ','.join(map(str, x)))
           .rename(columns={'topic_id': 'topic'})
          )
    return posts[['post_id']].drop_duplicates().merge(df1, how='left', on='post_id').fillna('Ambiguous!')

