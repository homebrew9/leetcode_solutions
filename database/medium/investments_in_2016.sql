-- Oracle
/* Write your PL/SQL query statement below */
select round(sum(x.tiv_2016), 2) as tiv_2016
  from Insurance x
 where exists (select null from Insurance y where y.pid != x.pid and y.tiv_2015 = x.tiv_2015)
   and not exists (select null from Insurance z where z.pid != x.pid and z.lat = x.lat and z.lon = x.lon)
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

