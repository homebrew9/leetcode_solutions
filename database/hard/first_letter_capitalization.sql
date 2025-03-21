-- Oracle
/* Write your PL/SQL query statement below */
with t_tokens (max_token_count) as (
    select max(regexp_count(content_text, '\S+') + regexp_count(content_text, '\s+')) as max_token_count
      from user_content
),
t1 (content_id, content_text, lvl, token, indx) as (
    select content_id, content_text, 1, regexp_substr(content_text, '(\S+|\s+)', 1, 1), regexp_instr(content_text, '(\S+|\s+)', 1, 1)
      from user_content
    union all
    select content_id, content_text, t1.lvl + 1, regexp_substr(content_text, '(\S+|\s+)', 1, t1.lvl + 1), regexp_instr(content_text, '(\S+|\s+)', 1, t1.lvl + 1)
      from t1
     where t1.lvl + 1 <= (select max_token_count from t_tokens)
),
t2 as (
    select content_id, content_text, lvl, initcap(token) as token, indx
      from t1
)
select content_id,
       content_text as original_text,
       listagg(token, '') within group (order by indx) as converted_text
  from t2
 group by content_id, content_text
 order by content_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
	select content_id,
		   content_text,
		   initcap(unnest(string_to_array(content_text, ' '))) as token
	from user_content
)
select content_id,
       content_text as original_text,
       string_agg(token, ' ') as converted_text
  from t
 group by content_id, content_text
 order by content_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_length (max_text_length) as (
    select max(len(content_text)) as max_text_length
	  from dbo.user_content
),
t_split (content_id, content_text, token, indx) as (
    select content_id, content_text, convert(varchar, substring(content_text, 1, 1)), 1
	  from dbo.user_content
	union all
	select ts.content_id, ts.content_text, convert(varchar, substring(ts.content_text, ts.indx+1, 1)), ts.indx+1
	  from t_split ts cross join t_length tl
	 where ts.indx + 1 <= tl.max_text_length
),
t as (
    select content_id, content_text, token, indx,
           lag(token) over (partition by content_id order by indx) as prev_token
      from t_split
),
t1 as (
    select content_id, content_text,
           case when indx=1 or prev_token=' ' then upper(token) else lower(token) end as token,
           indx, prev_token
      from t
)
select content_id, content_text as original_text,
       STRING_AGG(token, '') within group (order by indx) as converted_text
  from t1
 group by content_id, content_text
 order by content_id
;


# MySQL
# Write your MySQL query statement below
with recursive t_hier (n) as (
    select 1
    union all
    select th.n + 1
      from t_hier th
     where th.n <= (select max(length(content_text)) from user_content)
),
t as (
    select content_id, content_text, th.n,
           trim(substring(
                    substring_index(content_text, ' ', th.n),
                    length(substring_index(content_text, ' ', th.n - 1)) + 1
               )) as curr
      from user_content
           cross join t_hier th
     where trim(substring(
                    substring_index(content_text, ' ', th.n),
                    length(substring_index(content_text, ' ', th.n - 1)) + 1
               )) <> ''
     order by content_id, th.n
),
t1 as (
    select content_id, content_text, n, curr,
           concat(ucase(left(curr, 1)), lcase(substring(curr,2))) as upd_text
      from t
)
select content_id, content_text as original_text,
       group_concat(upd_text order by n separator ' ') as converted_text
  from t1
 group by content_id, content_text
;


# Pandas
import pandas as pd

def process_text(user_content: pd.DataFrame) -> pd.DataFrame:
    user_content['ct'] = user_content['content_text'].str.split()
    df = user_content.explode('ct')
    df['ct'] = df['ct'].str.capitalize()
    df = df.groupby(['content_id', 'content_text'], as_index=0)['ct'].agg(list)
    df['ct'] = df['ct'].apply(lambda x: ' '.join(map(str, x)))
    return df.rename(columns={'content_text': 'original_text', 'ct': 'converted_text'})

