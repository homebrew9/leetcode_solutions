-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
select d.name as department, e.name as employee, e.salary
  from employee e
       inner join department d on (d.id = e.departmentId)
       inner join (select e1.departmentId, max(e1.salary) as salary
                     from employee e1
                    group by e1.departmentId
                  ) x
       on (x.departmentId = d.id and x.salary = e.salary)
;


# Pandas

