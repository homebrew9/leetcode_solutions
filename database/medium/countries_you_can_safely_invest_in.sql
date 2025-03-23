-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (substr(p.phone_number,1,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (substr(p.phone_number,1,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (left(p.phone_number,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (substr(p.phone_number,1,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


# Pandas

