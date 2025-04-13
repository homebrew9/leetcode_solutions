-- Oracle
/* Write your PL/SQL query statement below */
select user_id, name, mail
from Users
where regexp_like(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$')
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select *
  from users
 where regexp_like (lower(mail), '^[a-z][a-z0-9_.-]*@leetcode\.com$')
;


-- SQL Server
/* Write your T-SQL query statement below */
select *
  from users
 where lower(left(mail,1)) like '[a-z]%'
   and lower(right(mail,13)) = '@leetcode.com'
   and lower(left(mail, len(mail)-13)) not like '%[^a-z0-9_.-]%'
;


# MySQL
# Write your MySQL query statement below
# MySQL uses C escape syntax, all backslashes in regexes should be doubled. https://dev.mysql.com/doc/refman/8.4/en/regexp.html
select *
  from users
 where regexp_like (lower(mail), '^[a-z][a-z0-9_.-]*@leetcode\\.com$')
;


# Pandas
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.match(r'^[a-zA-Z][\w\d.-]*@leetcode\.com$')]

