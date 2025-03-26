-- Oracle
/* Write your PL/SQL query statement below */
select 'bull' as word, (select count(*) from files where regexp_like(content, '\sbull\s')) as count from dual
union all
select 'bear' as word, (select count(*) from files where regexp_like(content, '\sbear\s')) as count from dual
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

