-- Oracle
/* Write your PL/SQL query statement below */
select floor((minute-1)/6)+1 as interval_no, sum(order_count) as total_orders
from orders
group by floor((minute-1)/6)+1
order by interval_no
;


-- PostgreSQL
-- Not sure why PostgreSQL is absent as an option in the drop-down.
select ceiling(minute / 6) as interval_no,
       sum(order_count)    as total_orders
  from orders
 group by ceiling(minute / 6)
 order by interval_no
;


-- SQL Server
/* Write your T-SQL query statement below */
select floor((minute-1)/6)+1 as interval_no, sum(order_count) as total_orders
from orders
group by floor((minute-1)/6)+1
order by interval_no
;


# MySQL
# Write your MySQL query statement below
select ceiling(minute / 6) as interval_no,
       sum(order_count)    as total_orders
  from orders
 group by ceiling(minute / 6)
 order by interval_no
;


# Pandas
# Note: There is no option for Pandas in the drop-down.
# For Pandas, we implement similar logic:
orders['interval_no'] = orders['minute'].apply(lambda x: math.ceil(x / 6))
return ( orders
        .groupby('interval_no', as_index=0)['order_count']
        .sum()
        .rename(columns={'order_count': 'total_orders'})
        .sort_values('interval_no')
       )

