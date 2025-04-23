-- Oracle


-- PostgreSQL


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

