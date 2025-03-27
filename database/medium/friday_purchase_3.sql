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
-- Write your PostgreSQL query statement below
with t (d) as (
    select generate_series(1,30) as d
),
t1 (dt) as (
    select '2023-11-01'::date + t.d - 1
      from t
),
t2 (dt, week_of_month, membership) as (
    select dt, to_char(dt, 'w')::int as week_of_month, m.membership
      from t1
           cross join (select 'Premium' as membership union all
                       select 'VIP'
                      ) as m
     where to_char(dt, 'fmDay') = 'Friday'
),
consolidated (purchase_date, membership, total_amount) as (
    select p.purchase_date, u.membership, sum(p.amount_spend) as total_amount
      from purchases p
           inner join users u on (u.user_id = p.user_id)
     group by p.purchase_date, u.membership
)
select t2.week_of_month, t2.membership, coalesce(c.total_amount, 0) as total_amount
  from t2
       left outer join consolidated c on (c.purchase_date = t2.dt and c.membership = t2.membership)
order by t2.week_of_month, t2.membership
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (dt, num) as (
    select convert(date, '2023-11-01') as dt, 0 as num
    union all
    select dateadd(day, 1, t.dt), t.num + 1
      from t
     where t.num + 1 < 30
),
t1 (dt, week_of_month, membership) as (
    select dt,
           datepart(week, dt) - datepart(week, '2023-11-01') + 1 as week_of_month,
           m.membership
      from t
           cross join (select 'Premium' as membership union all
                       select 'VIP'
                      ) m
     where datename(weekday, dt) = 'Friday'
),
consolidated (purchase_date, membership, total_amount) as (
    select p.purchase_date, u.membership, sum(p.amount_spend) as total_amount
      from purchases p
           inner join users u on (u.user_id = p.user_id)
     group by p.purchase_date, u.membership
)
select t1.week_of_month, t1.membership, coalesce(c.total_amount, 0) as total_amount
  from t1
       left outer join consolidated c on (c.purchase_date = t1.dt and c.membership = t1.membership)
order by t1.week_of_month, t1.membership
;


# MySQL
# Write your MySQL query statement below
with recursive t (dt, num) as (
    select '2023-11-01' as dt, 0 as num
    union all
    select t.dt + interval 1 day, t.num + 1
      from t
     where t.num + 1 < 30
),
t1 (dt, week_of_month, membership) as (
select dt,
       week(dt) - week('2023-11-01') + 1 as week_of_month,
       m.membership
  from t
       cross join (select 'Premium' as membership union all
                   select 'VIP'
                  ) m
 where dayname(dt) = 'Friday'
),
consolidated (purchase_date, membership, total_amount) as (
    select p.purchase_date, u.membership, sum(p.amount_spend) as total_amount
      from purchases p
           inner join users u on (u.user_id = p.user_id)
     group by p.purchase_date, u.membership
)
select t1.week_of_month, t1.membership, coalesce(c.total_amount, 0) as total_amount
  from t1
       left outer join consolidated c on (c.purchase_date = t1.dt and c.membership = t1.membership)
order by t1.week_of_month, t1.membership
;


# Pandas

