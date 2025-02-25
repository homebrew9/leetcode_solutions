-- Oracle
/* Write your PL/SQL query statement below */
with trx_iter (n) as (
    select 0 as n
      from dual
    union all
    select ti.n + 1
      from trx_iter ti
     where ti.n + 1 <= (select max(count(*)) from transactions group by user_id, transaction_date)
),
no_trx (transactions_count, visits_count) as (
select 0, count(*)
from visits v
where not exists (select null
                  from transactions t
                  where t.user_id = v.user_id
                  and t.transaction_date = v.visit_date
                 )
),
one_or_more_trx (transactions_count, visits_count) as (
select x.trx_count, count(*)
  from (
          select t.user_id, t.transaction_date, count(*) as trx_count
          from transactions t
          group by t.user_id, t.transaction_date
       ) x
 group by x.trx_count
)
select ti.n as transactions_count,
       coalesce(nt.visits_count, ot.visits_count, 0) as visits_count
from trx_iter ti
     left outer join no_trx nt on (nt.transactions_count = ti.n)
     left outer join one_or_more_trx ot on (ot.transactions_count = ti.n)
order by ti.n
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive trx_iter (n, max_cnt) as (
    select 0 as n, max(x.cnt) as max_cnt
      from ( select count(*) as cnt
             from transactions
             group by user_id, transaction_date
           ) x
    union all
    select ti.n + 1, ti.max_cnt
      from trx_iter ti
     where ti.n + 1 <= ti.max_cnt
),
no_trx (transactions_count, visits_count) as (
select 0, count(*)
from visits v
where not exists (select null
                  from transactions t
                  where t.user_id = v.user_id
                  and t.transaction_date = v.visit_date
                 )
),
one_or_more_trx (transactions_count, visits_count) as (
select x.trx_count, count(*)
  from (
          select t.user_id, t.transaction_date, count(*) as trx_count
          from transactions t
          group by t.user_id, t.transaction_date
       ) x
 group by x.trx_count
)
select ti.n as transactions_count,
       coalesce(nt.visits_count, ot.visits_count, 0) as visits_count
from trx_iter ti
     left outer join no_trx nt on (nt.transactions_count = ti.n)
     left outer join one_or_more_trx ot on (ot.transactions_count = ti.n)
order by ti.n
;


-- SQL Server
/* Write your T-SQL query statement below */
with trx_iter (n, max_cnt) as (
    select 0 as n, max(x.cnt) as max_cnt
      from ( select count(*) as cnt
             from transactions
             group by user_id, transaction_date
           ) x
    union all
    select ti.n + 1, ti.max_cnt
      from trx_iter ti
     where ti.n + 1 <= ti.max_cnt
),
no_trx (transactions_count, visits_count) as (
select 0, count(*)
from visits v
where not exists (select null
                  from transactions t
                  where t.user_id = v.user_id
                  and t.transaction_date = v.visit_date
                 )
),
one_or_more_trx (transactions_count, visits_count) as (
select x.trx_count, count(*)
  from (
          select t.user_id, t.transaction_date, count(*) as trx_count
          from transactions t
          group by t.user_id, t.transaction_date
       ) x
 group by x.trx_count
)
select ti.n as transactions_count,
       coalesce(nt.visits_count, ot.visits_count, 0) as visits_count
from trx_iter ti
     left outer join no_trx nt on (nt.transactions_count = ti.n)
     left outer join one_or_more_trx ot on (ot.transactions_count = ti.n)
order by ti.n
;


# MySQL
# Write your MySQL query statement below
with recursive trx_iter (n, max_cnt) as (
    select 0 as n, max(x.cnt) as max_cnt
      from ( select count(*) as cnt
             from transactions
             group by user_id, transaction_date
           ) x
    union all
    select ti.n + 1, ti.max_cnt
      from trx_iter ti
     where ti.n + 1 <= ti.max_cnt
),
no_trx (transactions_count, visits_count) as (
select 0, count(*)
from visits v
where not exists (select null
                  from transactions t
                  where t.user_id = v.user_id
                  and t.transaction_date = v.visit_date
                 )
),
one_or_more_trx (transactions_count, visits_count) as (
select x.trx_count, count(*)
  from (
          select t.user_id, t.transaction_date, count(*) as trx_count
          from transactions t
          group by t.user_id, t.transaction_date
       ) x
 group by x.trx_count
)
select ti.n as transactions_count,
       coalesce(nt.visits_count, ot.visits_count, 0) as visits_count
from trx_iter ti
     left outer join no_trx nt on (nt.transactions_count = ti.n)
     left outer join one_or_more_trx ot on (ot.transactions_count = ti.n)
order by ti.n
;

