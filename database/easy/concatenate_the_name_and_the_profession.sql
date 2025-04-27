-- Oracle
/* Write your PL/SQL query statement below */
select person_id, name||'('||substr(profession,1,1)||')' as name
from person
order by person_id desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select person_id, name||'('||substr(profession,1,1)||')' as name
from person
order by person_id desc
;


-- SQL Server
/* Write your T-SQL query statement below */
select person_id, name + '(' + substring(profession,1,1) + ')' as name
from person
order by person_id desc
;


# MySQL
# Write your MySQL query statement below
select person_id, concat(name, '(', substr(profession,1,1), ')') as name
from person
order by person_id desc
;


# Pandas
import pandas as pd

def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    person['name'] = person['name'] + '(' + person['profession'].str[:1] + ')'
    return person[['person_id','name']].sort_values(by='person_id', ascending=False)

