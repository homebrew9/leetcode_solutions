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
import pandas as pd
from datetime import datetime

def find_valid_users(purchases: pd.DataFrame, start_date: datetime, end_date: datetime, min_amount: int) -> pd.DataFrame:
    # Just to make sure that the "HMS" part is all zeros, irrespective of what is passed in!
    start_date = datetime.strptime(start_date.strftime('%Y%m%d')+' 00:00:00', '%Y%m%d %H:%M:%S')
    end_date = datetime.strptime(end_date.strftime('%Y%m%d')+' 00:00:00', '%Y%m%d %H:%M:%S')
    # Set up the filter conditions
    valid_start_time = purchases['time_stamp'] >= start_date
    valid_end_time = purchases['time_stamp'] <= end_date
    valid_amount = purchases['amount'] >= min_amount
    # Query, dedupe, sort, and return
    return ( purchases[valid_start_time & valid_end_time & valid_amount][['user_id']]
            .drop_duplicates()
            .sort_values('user_id')
           )

