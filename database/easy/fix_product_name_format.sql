-- Oracle
/* Write your PL/SQL query statement below */
select lower(trim(product_name)) as product_name,
       to_char(sale_date, 'yyyy-mm') as sale_date,
       count(*) as total
from sales
group by lower(trim(product_name)),
         to_char(sale_date, 'yyyy-mm')
order by 1,2
;


-- PostgreSQL
/* PostgreSQL is not available as an option in the drop-down.
   The Oracle query should, most likely, work for PostgreSQL too.
*/

-- SQL Server
/* Write your T-SQL query statement below */
select lower(trim(product_name)) as product_name,
       convert(varchar(7), sale_date, 120) as sale_date,
       count(*) as total
from sales
group by lower(trim(product_name)),
         convert(varchar(7), sale_date, 120)
order by 1,2
;


# MySQL
# Write your MySQL query statement below
select lower(trim(product_name)) as product_name,
       date_format(sale_date, '%Y-%m') as sale_date,
       count(*) as total
from sales
group by lower(trim(product_name)),
         date_format(sale_date, '%Y-%m')
order by 1,2
;


# Pandas
import pandas as pd

def fix_name_format(sales: pd.DataFrame) -> pd.DataFrame:
    # Fix the product name and sale date format
    sales['product_name'] = sales['product_name'].str.strip().str.lower()
    sales['sale_date'] = sales['sale_date'].dt.strftime('%Y-%m')
    
    # Group by product name and sale date, aggregate total sales, return sorted values
    return (  sales.groupby(by=['product_name','sale_date'],as_index=False)['sale_id']
              .count()
              .rename(columns={'sale_id':'total'})
              .sort_values(by=['product_name','sale_date'])
           )

