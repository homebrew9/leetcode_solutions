-- Oracle


-- PostgreSQL


-- SQL Server


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

