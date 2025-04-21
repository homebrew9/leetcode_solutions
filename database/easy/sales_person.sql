-- Oracle
/* Write your PL/SQL query statement below */
select s1.name
  from salesperson s1
 where s1.sales_id not in (
     select s.sales_id
       from orders o
            inner join salesperson s on (s.sales_id = o.sales_id)
            inner join company c on (c.com_id = o.com_id and c.name = 'RED')
 )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select s1.name
  from salesperson s1
 where s1.sales_id not in (
     select s.sales_id
       from orders o
            inner join salesperson s on (s.sales_id = o.sales_id)
            inner join company c on (c.com_id = o.com_id and c.name = 'RED')
 )
;


-- SQL Server
/* Write your T-SQL query statement below */
select s1.name
  from salesperson s1
 where s1.sales_id not in (
     select s.sales_id
       from orders o
            inner join salesperson s on (s.sales_id = o.sales_id)
            inner join company c on (c.com_id = o.com_id and c.name = 'RED')
 )
;


# MySQL
# Write your MySQL query statement below
select s.name
from salesperson s
where not exists (
    select null
    from orders o
         inner join company c on (c.com_id = o.com_id and c.name = 'RED')
    where o.sales_id = s.sales_id
)
;


# Pandas
import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = company.merge(orders, how='inner', on='com_id')
    df1 = df[df['name']=='RED'].sales_id
    return sales_person[~sales_person.sales_id.isin(df1)][['name']]

