-- Oracle


-- PostgreSQL
CREATE OR REPLACE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT)
RETURNS TABLE (user_id INT) AS $$
BEGIN
  RETURN QUERY (
      -- Write your PostgreSQL query statement below.
   select distinct p.user_id
      from purchases p
     where p.time_stamp between startDate and endDate
       and p.amount >= minAmount
     order by p.user_id
  );
END;
$$ LANGUAGE plpgsql;


-- SQL Server
CREATE PROCEDURE getUserIDs(@startDate DATE, @endDate DATE, @minAmount INT) AS
BEGIN
    /* Write your T-SQL query statement below. */
   select distinct p.user_id
      from purchases p
     where p.time_stamp between @startDate and @endDate
       and p.amount >= @minAmount
     order by p.user_id;
END


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

