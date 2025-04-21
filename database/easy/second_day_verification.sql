-- Oracle
/* Write your PL/SQL query statement below */
select e.user_id
  from emails e
       inner join texts t on (t.email_id = e.email_id and
                              t.signup_action = 'Verified' and
                              trunc(t.action_date) = trunc(e.signup_date) + 1
                             )
order by e.user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e.user_id
  from emails e
       inner join texts t on (t.email_id = e.email_id and
                              t.signup_action = 'Verified' and
                              date_trunc('day', t.action_date) = date_trunc('day', e.signup_date) + interval '1 day'
                             )
order by e.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
-- DATETRUNC(day, <my_datetime2>) works in SQL Server 2022
-- In SQL Server 2019, convert <my_datetime2> to date
select e.user_id
  from emails e
       inner join texts t on (t.email_id = e.email_id and
                              t.signup_action = 'Verified' and
                              convert(date, t.action_date) = dateadd(day, 1, convert(date, e.signup_date))
                             )
order by e.user_id
;


# MySQL
# Write your MySQL query statement below
select e.user_id
  from emails e
       inner join texts t on (t.email_id = e.email_id and
                              t.signup_action = 'Verified' and
                              date(t.action_date) = date(e.signup_date) + interval 1 day
                             )
order by e.user_id
;


# Pandas
import pandas as pd
import datetime

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    emails['date_after_signup_date'] = emails['signup_date'].dt.floor('d') + datetime.timedelta(days=1)
    texts['action_date_fmt'] = texts['action_date'].dt.floor('d')
    return (emails
            .merge(texts,
                   how='inner',
                   left_on=['email_id','date_after_signup_date'],
                   right_on=['email_id','action_date_fmt']
                  )
            .query('signup_action == "Verified"')[['user_id']]
            .sort_values(by='user_id')
           )

