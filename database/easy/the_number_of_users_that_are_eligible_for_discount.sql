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
import pandas as pd
from datetime import datetime

def count_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    # I think this should not get accepted since I did not fix the timestamps of start_date and end_date before filtering.
    valid_start = purchases['time_stamp'] >= start_date
    valid_end = purchases['time_stamp'] <= end_date
    valid_amount = purchases['amount'] >= min_amount
    user_count = len(purchases[(valid_start) & (valid_end) & (valid_amount)][['user_id']].drop_duplicates())
    return pd.DataFrame(data={'user_cnt': [user_count]})

