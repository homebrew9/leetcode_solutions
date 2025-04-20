-- Oracle
/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 */
delete from person
 where id in (
                select id
                  from (select id, email, dense_rank() over (partition by email order by id) as drnk from person) x
                 where drnk > 1
             )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- PostgreSQL "delete join" statement
with t (id, email, drnk) as (
    select id, email, dense_rank() over (partition by email order by id) as drnk
      from person
)
delete
  from person p
 using t
 where p.id = t.id and t.drnk > 1
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Note that "delete using join" statement in SQL Server requires
-- the table name or alias between "delete" and "from" i.e.
-- "delete p from ..." instead of "delete from"
--
with t (id, email, drnk) as (
    select id, email, dense_rank() over (partition by email order by id) as drnk
      from person
)
delete p
  from person p
       join t on (t.id = p.id and t.drnk > 1)
;


# MySQL
# Write your MySQL query statement below
delete p1
  from Person p1,
       Person p2
 where p1.Email = p2.Email
   and p1.Id > p2.Id
;


# Pandas
import pandas as pd
from copy import deepcopy

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', inplace=True)

