-- Oracle
CREATE FUNCTION getUserIDs(startDate IN DATE, endDate IN DATE, minAmount IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select count(distinct user_id)
      into result
      from purchases
     where time_stamp between startDate and endDate
       and amount >= minAmount;
    RETURN result;
END;


-- PostgreSQL
CREATE OR REPLACE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT AS $$
BEGIN
  RETURN (
	  -- Write your PostgreSQL query statement below.
      select count(distinct user_id)
        from purchases
       where time_stamp between startDate and endDate
         and amount >= minAmount
  );
END;
$$ LANGUAGE plpgsql;


-- SQL Server
CREATE FUNCTION getUserIDs(@startDate DATE, @endDate DATE, @minAmount INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
      select count(distinct user_id)
        from purchases
       where time_stamp between @startDate and @endDate
         and amount >= @minAmount
    );
END


# MySQL
CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select count(distinct user_id)
        from purchases
       where time_stamp between startDate and endDate
         and amount >= minAmount
  );
END


# Pandas

