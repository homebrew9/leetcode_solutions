-- Oracle
/* Write your PL/SQL query statement below */
select content_id, content_text as original_text, initcap(content_text) as converted_text
from user_content
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select content_id, content_text as original_text, initcap(content_text) as converted_text
from user_content
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_maxlen (max_length) as (
    select max(len(content_text)) as max_length
      from user_content
),
iter (pos) as (
    select 1 as pos
    union all
    select i.pos + 1
      from iter i cross join t_maxlen tm
     where i.pos + 1 <= tm.max_length
),
t as (
    select content_id, content_text, iter.pos,
           substring(content_text, iter.pos, 1) as token,
           lag(substring(content_text, iter.pos, 1)) over (partition by content_id order by iter.pos) as prev_token
      from user_content
           cross join iter
     where substring(content_text, iter.pos, 1) is not null
)
select content_id, content_text as original_text,
       string_agg(case when prev_token is null or prev_token in (' ', '-') then upper(token)
                       else lower(token)
                  end, '') within group (order by pos) as converted_text
  from t
group by content_id, content_text
order by content_id
;


# MySQL
# Write your MySQL query statement below
with recursive iter (pos) as (
    select 1 as pos
    union all
    select i.pos + 1
      from iter i
     where i.pos + 1 <= (select max(length(content_text)) from user_content)
),
t as (
    select content_id, content_text, iter.pos,
           substring(content_text, iter.pos, 1) as token,
           lag(substring(content_text, iter.pos, 1)) over (partition by content_id order by iter.pos) as prev_token
    from user_content
         cross join iter
   where substring(content_text, iter.pos, 1) is not null
)
select content_id, content_text as original_text,
       group_concat(case when prev_token is null or prev_token in (' ', '-') then upper(token)
                         else lower(token)
                    end order by pos separator ''
                   ) as converted_text
  from t
group by content_id, content_text
;


# Pandas
import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content['converted_text'] = user_content['content_text'].str.title()
    return user_content.rename(columns={'content_text': 'original_text'})

