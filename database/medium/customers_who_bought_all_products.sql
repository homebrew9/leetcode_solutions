-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select distinct t.customer_id
  from customer t
 where t.customer_id not in (
                               select x.customer_id
                                 from (
                                            select distinct c.customer_id, p.product_key
                                              from customer c
                                                   cross join product p
                                      ) x
                                      left outer join
                                      (select m.customer_id, m.product_key
                                         from customer m
                                                       inner join product n on (n.product_key = m.product_key)
                                      ) y
                                      on (x.customer_id = y.customer_id and x.product_key = y.product_key)
                                where y.product_key is null
                            )
;


# MySQL
# Write your MySQL query statement below
select distinct t.customer_id
  from customer t
 where t.customer_id not in (
                               select x.customer_id
                                 from (
                                            select distinct c.customer_id, p.product_key
                                              from customer c
                                                   cross join product p
                                      ) x
                                      left outer join
                                      (select m.customer_id, m.product_key
                                         from customer m
                                                       inner join product n on (n.product_key = m.product_key)
                                      ) y
                                      on (x.customer_id = y.customer_id and x.product_key = y.product_key)
                                where y.product_key is null
                            )
;


# Pandas
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_count = len(product)
    return ( customer
            .drop_duplicates()
            .groupby('customer_id', as_index=0)['product_key']
            .count()
            .query('product_key == @product_count')[['customer_id']]
           )

