-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
select regexp_replace(email, '^.*@(.*)$', '\1') as email_domain, count(*) as count
from emails
where regexp_like(email, '^.*\@\w+\.com')
group by regexp_replace(email, '^.*@(.*)$', '\1')
order by email_domain
;


-- SQL Server
/* Write your T-SQL query statement below */
select substring(email, charindex('@', email)+1, len(email)) as email_domain,
       count(*) as count
from emails
where email like '%.com'
group by substring(email, charindex('@', email)+1, len(email))
order by email_domain
;


# MySQL
# Write your MySQL query statement below
select substr(email, instr(email, '@')+1) as email_domain, count(*) as count
from emails
where email like '%.com'
group by substr(email, instr(email, '@')+1)
order by email_domain
;


# Pandas
import pandas as pd

def find_unique_email_domains(emails: pd.DataFrame) -> pd.DataFrame:
    emails = emails[emails['email'].str.endswith('.com')]
    emails['email_domain'] = emails['email'].str.extract('@(.*)$')
    return ( emails
            .groupby('email_domain', as_index=0)['id']
            .count()
            .rename(columns={'id': 'count'})
            .sort_values('email_domain')
           )

