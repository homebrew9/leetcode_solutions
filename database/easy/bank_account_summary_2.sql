-- Oracle
/* Write your PL/SQL query statement below */
select u.name, sum(t.amount) as balance
  from users u
       inner join transactions t on (t.account = u.account)
 group by u.name
having sum(t.amount) > 10000
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

