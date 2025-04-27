-- Oracle
/* Write your PL/SQL query statement below */
select p.firstName, p.lastName, a.city, a.state
  from person p
       left outer join address a on (a.personId = p.personId)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.firstName, p.lastName, a.city, a.state
  from person p
       left outer join address a on (a.personId = p.personId)
;


-- SQL Server
/* Write your T-SQL query statement below */
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
     LEFT OUTER JOIN Address a ON (a.personId = p.personId)
;


# MySQL
# Write your MySQL query statement below
select p.firstname, p.lastname, a.city, a.state
from person p
     left outer join address a on (a.personid = p.personid)
;


# Pandas
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address, how='left', on='personId')[['firstName','lastName','city','state']]

