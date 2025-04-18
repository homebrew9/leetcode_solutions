-- Oracle
/* Write your PL/SQL query statement below */
select s.seller_name
  from seller s
 where not exists (select null
                     from orders o
                    where o.seller_id = s.seller_id
                      and to_char(sale_date, 'yyyy') = '2020'
                  )
order by s.seller_name
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

