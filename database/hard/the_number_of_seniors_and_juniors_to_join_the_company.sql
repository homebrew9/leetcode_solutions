-- Oracle
/* Write your PL/SQL query statement below */
with t1 as (
select employee_id, salary,
       sum(salary) over (order by salary rows between unbounded preceding and current row) as total_salary,
       count(employee_id) over (order by salary rows between unbounded preceding and current row) as candidate_count,
       70000 - sum(salary) over (order by salary rows between unbounded preceding and current row) as leftover_amount
from candidates
where experience = 'Senior'
),
senior_count as (
select candidate_count, leftover_amount
from t1
where candidate_count = (select max(candidate_count) from t1 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t1
where not exists (select null from t1 where leftover_amount >= 0)
),
t2 as (
select c.employee_id, c.salary,
       sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as total_salary,
       count(c.employee_id) over (order by c.salary rows between unbounded preceding and current row) as candidate_count,
       sc.leftover_amount - sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as leftover_amount
from candidates c
     cross join senior_count sc
where c.experience = 'Junior'
),
junior_count as (
select candidate_count, leftover_amount
from t2
where candidate_count = (select max(candidate_count) from t2 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t2
where not exists (select null from t2 where leftover_amount >= 0)
)
select 'Senior' as experience, candidate_count as accepted_candidates
from senior_count
union all
select 'Junior', candidate_count
from junior_count
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t1 as (
select employee_id, salary,
       sum(salary) over (order by salary rows between unbounded preceding and current row) as total_salary,
       count(employee_id) over (order by salary rows between unbounded preceding and current row) as candidate_count,
       70000 - sum(salary) over (order by salary rows between unbounded preceding and current row) as leftover_amount
from candidates
where experience = 'Senior'
),
senior_count as (
select candidate_count, leftover_amount
from t1
where candidate_count = (select max(candidate_count) from t1 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t1
where not exists (select null from t1 where leftover_amount >= 0)
),
t2 as (
select c.employee_id, c.salary,
       sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as total_salary,
       count(c.employee_id) over (order by c.salary rows between unbounded preceding and current row) as candidate_count,
       sc.leftover_amount - sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as leftover_amount
from candidates c
     cross join senior_count sc
where c.experience = 'Junior'
),
junior_count as (
select candidate_count, leftover_amount
from t2
where candidate_count = (select max(candidate_count) from t2 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t2
where not exists (select null from t2 where leftover_amount >= 0)
)
select 'Senior' as experience, candidate_count as accepted_candidates
from senior_count
union all
select 'Junior', candidate_count
from junior_count
;


-- SQL Server
/* Write your T-SQL query statement below */
with t1 as (
select employee_id, salary,
       sum(salary) over (order by salary rows between unbounded preceding and current row) as total_salary,
       count(employee_id) over (order by salary rows between unbounded preceding and current row) as candidate_count,
       70000 - sum(salary) over (order by salary rows between unbounded preceding and current row) as leftover_amount
from candidates
where experience = 'Senior'
),
senior_count as (
select candidate_count, leftover_amount
from t1
where candidate_count = (select max(candidate_count) from t1 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t1
where not exists (select null from t1 where leftover_amount >= 0)
),
t2 as (
select c.employee_id, c.salary,
       sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as total_salary,
       count(c.employee_id) over (order by c.salary rows between unbounded preceding and current row) as candidate_count,
       sc.leftover_amount - sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as leftover_amount
from candidates c
     cross join senior_count sc
where c.experience = 'Junior'
),
junior_count as (
select candidate_count, leftover_amount
from t2
where candidate_count = (select max(candidate_count) from t2 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t2
where not exists (select null from t2 where leftover_amount >= 0)
)
select 'Senior' as experience, candidate_count as accepted_candidates
from senior_count
union all
select 'Junior', candidate_count
from junior_count
;


# MySQL
# Write your MySQL query statement below
with t1 as (
select employee_id, salary,
       sum(salary) over (order by salary rows between unbounded preceding and current row) as total_salary,
       count(employee_id) over (order by salary rows between unbounded preceding and current row) as candidate_count,
       70000 - sum(salary) over (order by salary rows between unbounded preceding and current row) as leftover_amount
from candidates
where experience = 'Senior'
),
senior_count as (
select candidate_count, leftover_amount
from t1
where candidate_count = (select max(candidate_count) from t1 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t1
where not exists (select null from t1 where leftover_amount >= 0)
),
t2 as (
select c.employee_id, c.salary,
       sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as total_salary,
       count(c.employee_id) over (order by c.salary rows between unbounded preceding and current row) as candidate_count,
       sc.leftover_amount - sum(c.salary) over (order by c.salary rows between unbounded preceding and current row) as leftover_amount
from candidates c
     cross join senior_count sc
where c.experience = 'Junior'
),
junior_count as (
select candidate_count, leftover_amount
from t2
where candidate_count = (select max(candidate_count) from t2 where leftover_amount >= 0)
union all
select distinct 0, 70000
from t2
where not exists (select null from t2 where leftover_amount >= 0)
)
select 'Senior' as experience, candidate_count as accepted_candidates
from senior_count
union all
select 'Junior', candidate_count
from junior_count
;

