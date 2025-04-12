-- Oracle
/* Write your PL/SQL query statement below */
select stock_name,
       sum(case operation when 'Sell' then price end) - sum(case operation when 'Buy' then price end) as "capital_gain_loss"
  from stocks
 group by stock_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select stock_name, sum(case when operation='Sell' then price else 0 end) -
                   sum(case when operation='Buy' then price else 0 end) as capital_gain_loss
from stocks
group by stock_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select stock_name, sum(case when operation='Sell' then price else 0 end) -
                   sum(case when operation='Buy' then price else 0 end) as capital_gain_loss
from stocks
group by stock_name
;


# MySQL
# Write your MySQL query statement below
select stock_name, sum(case when operation='Sell' then price else 0 end) -
                   sum(case when operation='Buy' then price else 0 end) as capital_gain_loss
from stocks
group by stock_name
;


# Pandas
import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['price'] = np.where(stocks['operation'] == 'Buy', -stocks['price'], stocks['price'])
    return ( stocks
            .groupby('stock_name', as_index=0)['price']
            .sum()
            .rename(columns={'price': 'capital_gain_loss'})
           )

