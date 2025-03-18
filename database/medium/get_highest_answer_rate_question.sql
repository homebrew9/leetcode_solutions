-- Oracle
/* Write your PL/SQL query statement below */
with t (question_id, answer_rate) as (
select question_id,
       sum(case when action = 'answer' then 1 else 0 end)
       /
       sum(case when action = 'show' then 1 else 0 end) as answer_rate
from SurveyLog
group by question_id
)
,
t1 as (
select question_id, answer_rate,
       dense_rank() over (partition by answer_rate order by question_id) as drnk
from t
)
select question_id as survey_log
from t1
where answer_rate = (select max(answer_rate) from t1)
and drnk = 1;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (question_id, answer_rate) as (
select question_id,
       sum(case when action = 'answer' then 1 else 0 end)::numeric
       /
       sum(case when action = 'show' then 1 else 0 end)::numeric as answer_rate
from SurveyLog
group by question_id
)
,
t1 as (
select question_id, answer_rate,
       dense_rank() over (partition by answer_rate order by question_id) as drnk
from t
)
select question_id as survey_log
from t1
where answer_rate = (select max(answer_rate) from t1)
and drnk = 1;


-- SQL Server


# MySQL
# Write your MySQL query statement below
with t (question_id, answer_rate) as (
select question_id,
       sum(case when action = 'answer' then 1 else 0 end)
       /
       sum(case when action = 'show' then 1 else 0 end) as answer_rate
from SurveyLog
group by question_id
)
,
t1 as (
select question_id, answer_rate,
       dense_rank() over (partition by answer_rate order by question_id) as drnk
from t
)
select question_id as survey_log
from t1
where answer_rate = (select max(answer_rate) from t1)
and drnk = 1
;


# Pandas
import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    df1 = ( survey_log[survey_log['action']=='answer']
           .groupby('question_id', as_index=False)['id']
           .count()
           .rename(columns={'id':'answer_count'})
          )
    df2 = ( survey_log[survey_log['action']=='show']
           .groupby('question_id', as_index=False)['id']
           .count()
           .rename(columns={'id':'show_count'})
          )
    df = df1.merge(df2, how='outer', on='question_id').fillna(0)
    df['answer_rate'] = df['answer_count']/df['show_count']
    max_answer_rate = df['answer_rate'].max()
    return ( df[df['answer_rate']==max_answer_rate]
            .groupby('answer_rate', as_index=False)['question_id']
            .min()[['question_id']]
            .rename(columns={'question_id': 'survey_log'})
           )

