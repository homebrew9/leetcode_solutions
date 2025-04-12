-- Oracle
/* Write your PL/SQL query statement below */
select to_char(sale_date, 'yyyy-mm-dd') as sale_date,
       sum(case when fruit = 'oranges' then -sold_num else sold_num end) as diff
  from sales
 group by sale_date
 order by sale_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select x.sale_date, x.sold_num - y.sold_num as diff
from (select sale_date, sold_num from sales where fruit = 'apples') x
     inner join
     (select sale_date, sold_num from sales where fruit = 'oranges') y
     on (x.sale_date = y.sale_date)
order by x.sale_date
;


-- SQL Server
/* Write your T-SQL query statement below */
select x.sale_date, x.sold_num - y.sold_num as diff
from (select sale_date, sold_num from sales where fruit = 'apples') x
     inner join
     (select sale_date, sold_num from sales where fruit = 'oranges') y
     on (x.sale_date = y.sale_date)
order by x.sale_date
;


# MySQL
# Write your MySQL query statement below
select x.sale_date, x.sold_num - y.sold_num as diff
from (select sale_date, sold_num from sales where fruit = 'apples') x
     inner join
     (select sale_date, sold_num from sales where fruit = 'oranges') y
     on (x.sale_date = y.sale_date)
order by x.sale_date
;


# Pandas
import pandas as pd

def apples_oranges(sales: pd.DataFrame) -> pd.DataFrame:
    apple_sales = sales[sales['fruit'] == 'apples'][['sale_date', 'sold_num']]
    orange_sales = sales[sales['fruit'] == 'oranges'][['sale_date', 'sold_num']]
    df = (  apple_sales.merge(orange_sales, how='inner', on='sale_date')
                       .rename(columns={'sold_num_x':'apples_sold', 'sold_num_y':'oranges_sold'})
         )
    df['diff'] = df['apples_sold'] - df['oranges_sold']
    return df[['sale_date', 'diff']].sort_values(by='sale_date')

