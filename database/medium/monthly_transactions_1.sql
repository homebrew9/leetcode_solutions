-- Oracle
/* Write your PL/SQL query statement below */
select to_char(trans_date, 'YYYY-MM') as month,
       country,
       count(*) as trans_count,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(amount) as trans_total_amount,
       sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by to_char(trans_date, 'YYYY-MM'), country
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select to_char(trans_date, 'yyyy-mm') as month,
       country,
	   count(*) as trans_count,
	   sum(case when state = 'approved' then 1 else 0 end) as approved_count,
	   sum(amount) as trans_total_amount,
	   sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
  from transactions
 group by to_char(trans_date, 'yyyy-mm'),
          country
;


-- SQL Server
select left(convert(varchar(max), trans_date, 23), 7) as month,
       country,
	   count(*) as trans_count,
	   sum(case when state = 'approved' then 1 else 0 end) as approved_count,
	   sum(amount) as trans_total_amount,
	   sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
  from transactions
 group by left(convert(varchar(max), trans_date, 23), 7), country
;


# MySQL
# Write your MySQL query statement below
select date_format(trans_date, '%Y-%m') as month,
       country,
       count(*) as trans_count,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(amount) as trans_total_amount,
       sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
  from transactions
 group by date_format(trans_date, '%Y-%m'), country
;


# Pandas

