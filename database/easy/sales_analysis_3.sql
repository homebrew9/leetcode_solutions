-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select p.product_id, min(s.sale_date) as min_sd, max(s.sale_date) as max_sd
      from Product p, Sales s
     where p.product_id = s.product_id
     group by p.product_id
),
t1 as (
    select product_id, min_sd, max_sd
      from t
     where trunc(min_sd) between TO_DATE('2019-01-01','YYYY-MM-DD') and TO_DATE('2019-03-31','YYYY-MM-DD')
       and trunc(max_sd) between TO_DATE('2019-01-01','YYYY-MM-DD') and TO_DATE('2019-03-31','YYYY-MM-DD')
)
select t1.product_id, p.product_name
  from t1, Product p
 where t1.product_id = p.product_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.product_id, p.product_name
  from product p
 where exists ( select null
                  from sales s1
                 where s1.product_id = p.product_id
                   and s1.sale_date between '2019-01-01'::date and '2019-03-31'::date
              )
and not exists ( select null
                   from sales s2
                  where s2.product_id = p.product_id
                    and (s2.sale_date < '2019-01-01'::date or s2.sale_date > '2019-03-31'::date)
               )
;


-- SQL Server
/* Write your T-SQL query statement below */
SELECT p.product_id, p.product_name
  FROM Sales s
       LEFT JOIN Product p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'
;

/* Write your T-SQL query statement below */
select distinct s.product_id, p.product_name
  from sales s
       join product p ON s.product_id = p.product_id
 where sale_date between '2019-01-01' and '2019-03-31'
   and s.product_id not in (select distinct s1.product_id
                              from sales s1
                             where s1.sale_date not between '2019-01-01' and '2019-03-31'
                           )
;


# MySQL
# Write your MySQL query statement below
select distinct s.product_id, p.product_name
  from sales s
       join product p ON s.product_id = p.product_id
 where sale_date between '2019-01-01' and '2019-03-31'
   and s.product_id not in (select distinct product_id
                              from sales
                             where sale_date not between '2019-01-01' and '2019-03-31'
                           )
;


# Pandas
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sold_in_first_qtr = ( sales
                         .query('"2019-01-01" <= sale_date <= "2019-03-31"')[['product_id']]
                         .drop_duplicates()
                        )
    sold_outside_of_first_qtr = ( sales
                                 .query('sale_date < "2019-01-01" or sale_date > "2019-03-31"')[['product_id']]
                                 .drop_duplicates()
                                )
    return ( sold_in_first_qtr[~sold_in_first_qtr['product_id'].isin(sold_outside_of_first_qtr['product_id'])]
            .merge(product, how='inner', on='product_id')[['product_id','product_name']]
           )

