-- Oracle
/* Write your PL/SQL query statement below */
select to_char(trans_date, 'YYYY-MM') as month,
       country,
       count(*) as trans_count,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(amount) as trans_total_amount,
       sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by to_char(trans_date, 'YYYY-MM'), country
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select to_char(trans_date, 'yyyy-mm') as month,
       country,
	   count(*) as trans_count,
	   sum(case when state = 'approved' then 1 else 0 end) as approved_count,
	   sum(amount) as trans_total_amount,
	   sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
  from transactions
 group by to_char(trans_date, 'yyyy-mm'),
          country
;


-- SQL Server
select left(convert(varchar(max), trans_date, 23), 7) as month,
       country,
	   count(*) as trans_count,
	   sum(case when state = 'approved' then 1 else 0 end) as approved_count,
	   sum(amount) as trans_total_amount,
	   sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
  from transactions
 group by left(convert(varchar(max), trans_date, 23), 7), country
;


# MySQL
# Write your MySQL query statement below
select date_format(trans_date, '%Y-%m') as month,
       country,
       count(*) as trans_count,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(amount) as trans_total_amount,
       sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
  from transactions
 group by date_format(trans_date, '%Y-%m'), country
;


# Pandas
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['approved_count'] = np.where(transactions['state']=='approved', 1, 0)
    transactions['approved_total_amount'] = np.where(transactions['state']=='approved', transactions['amount'], 0)
    return ( transactions
            .groupby(['month', 'country'], dropna=False, as_index=0)
            .agg({'id': 'count', 'approved_count': 'sum', 'amount': 'sum', 'approved_total_amount': 'sum'})
            .rename(columns={'id': 'trans_count', 'amount': 'trans_total_amount'})
           )

