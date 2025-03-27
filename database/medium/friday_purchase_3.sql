-- Oracle
/* Write your PL/SQL query statement below */
with t (dt) as (
    select DATE'2023-11-01' + level - 1 as dt
      from dual
   connect by level <= 30
),
t1 (dt, week_of_month, membership) as (
    select dt, to_number(to_char(dt, 'w')) as week_of_month, m.membership
      from t
           cross join (select 'Premium' as membership from dual union all
                       select 'VIP' from dual
                      ) m
     where to_char(dt, 'fmDay') = 'Friday'
),
consolidated (purchase_date, membership, total_amount) as (
    select p.purchase_date, u.membership, sum(p.amount_spend) as total_amount
      from purchases p
           inner join users u on (u.user_id = p.user_id)
     group by p.purchase_date, u.membership
)
select t1.week_of_month, t1.membership, nvl(c.total_amount, 0) as total_amount
  from t1
       left outer join consolidated c on (c.purchase_date = t1.dt and c.membership = t1.membership)
order by t1.week_of_month, t1.membership
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

