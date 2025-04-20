-- Oracle
/* Write your PL/SQL query statement below */
select distinct a.user_id
from loans a
     inner join loans b on (b.user_id = a.user_id and b.loan_type = 'Refinance')
     inner join loans c on (c.user_id = a.user_id and c.loan_type = 'Mortgage')
order by a.user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct l.user_id
  from loans l
 where exists (select null from loans l1 where l1.user_id = l.user_id and l1.loan_type = 'Refinance')
   and exists (select null from loans l2 where l2.user_id = l.user_id and l2.loan_type = 'Mortgage')
 order by l.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct a.user_id
from loans a
     inner join loans b on (b.user_id = a.user_id and b.loan_type = 'Refinance')
     inner join loans c on (c.user_id = a.user_id and c.loan_type = 'Mortgage')
order by a.user_id
;


# MySQL
# Write your MySQL query statement below
select distinct a.user_id
from loans a
     inner join loans b on (b.user_id = a.user_id and b.loan_type = 'Refinance')
     inner join loans c on (c.user_id = a.user_id and c.loan_type = 'Mortgage')
order by a.user_id
;


# Pandas
import pandas as pd

def loan_types(loans: pd.DataFrame) -> pd.DataFrame:
    return ( pd
            .merge(loans[loans['loan_type']=='Mortgage'],
                   loans[loans['loan_type']=='Refinance'],
                   how='inner', on='user_id'
                  )[['user_id']]
            .drop_duplicates()
            .sort_values('user_id')
           )

