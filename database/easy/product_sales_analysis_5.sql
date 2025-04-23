-- Oracle
/* Write your PL/SQL query statement below */
select s.user_id, sum(s.quantity*p.price) as spending
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id
order by spending desc, user_id
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select s.user_id, sum(s.quantity*p.price) as spending
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id
order by spending desc, user_id
;


# MySQL
# Write your MySQL query statement below
select s.user_id, sum(s.quantity*p.price) as spending
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id
order by spending desc, user_id
;


# Pandas
import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, how='inner', on='product_id')
    df['spending'] = df['quantity']*df['price']
    return (  df.groupby('user_id', as_index=False)['spending']
                .sum()[['user_id','spending']]
                .sort_values(by=['spending','user_id'], ascending=[False,True])
           )

