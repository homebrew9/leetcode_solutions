-- Oracle
/* Write your PL/SQL query statement below */
select email
  from person
 group by email
having count(*) > 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select email
  from person
 group by email
having count(*) > 1
;


-- SQL Server
/* Write your T-SQL query statement below */
select email as Email
from Person
group by email
having count(*) > 1
;


# MySQL
# Write your MySQL query statement below
select email
from person
group by email
having count(*) > 1
;


# Pandas
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.groupby('email', as_index=0)['id'].count().query('id > 1')[['email']]

