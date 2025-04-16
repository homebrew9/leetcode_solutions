-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
   select distinct p.user_id
      from purchases p
     where p.time_stamp between startDate and endDate
       and p.amount >= minAmount
     order by p.user_id;
END


# Pandas

