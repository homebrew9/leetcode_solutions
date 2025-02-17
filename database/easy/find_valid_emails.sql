-- Oracle
/* Write your PL/SQL query statement below */
select user_id, email
from users
where regexp_like(email, '^[a-zA-Z0-9_]+@[a-zA-Z].*\.com$')
order by user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select user_id, email
from users
where regexp_like(email, '^[a-zA-Z0-9_]+@[a-zA-Z].*\.com$')
order by user_id
;


# MySQL
# Write your MySQL query statement below
select user_id, email
from users
where regexp_like(email, '^[a-zA-Z0-9_]+@[a-zA-Z].*\.com$')
order by user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select user_id, email
  from users
 where len(email) - len(replace(email, '@', '')) = 1
   and upper(right(email, 4)) = '.COM'
   and upper(substring(email, 1, charindex('@', email) - 1)) not like '%[^A-Z0-9_]%'
   and upper(substring(email, charindex('@', email) + 1, len(email))) not like '%[^A-Z.]%'
;


# Pandas - Solution 1
import pandas as pd
import re

def is_valid(email):
    if len(re.findall(r'@', email)) != 1:
        return False
    if email[-4:].lower() != '.com':
        return False
    left_part, right_part = [x.lower() for x in email.split('@')]
    if not re.match(r'^\w+$', left_part):
        return False
    if not re.match(r'^[a-z.]+$', right_part):
        return False
    return True

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['email'].apply(is_valid)].sort_values('user_id')
    

# Pandas - Solution 2
import pandas as pd
import re

def is_valid(email):
    if re.search(r'^\w+@[a-z]+.com$', email.lower()):
        return True
    return False

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['email'].apply(is_valid)].sort_values('user_id')

