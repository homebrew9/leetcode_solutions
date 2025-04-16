-- Oracle
CREATE FUNCTION getUserIDs(startDate IN DATE, endDate IN DATE, minAmount IN NUMBER)
RETURN SYS_REFCURSOR IS result SYS_REFCURSOR;
BEGIN
    /* Write your PL/SQL query statement below */
   open result for
   select distinct user_id
      from purchases
     where time_stamp between startDate and endDate
       and amount >= minAmount
     order by user_id;
    RETURN result;
END;


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

