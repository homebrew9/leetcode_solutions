-- Oracle
/* Write your PL/SQL query statement below */
WITH t AS (
select f1.policy_id, f1.state, f1.fraud_score,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score) AS cnt_higher_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state) AS total_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score) /
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state) AS top_percentile_score
from fraud f1
)
SELECT policy_id, state, fraud_score
FROM t
WHERE t.top_percentile_score <= 0.05
ORDER BY state, fraud_score DESC, policy_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
WITH t AS (
select f1.policy_id, f1.state, f1.fraud_score,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score) AS cnt_higher_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state) AS total_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score)::numeric /
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state)::numeric AS top_percentile_score
from fraud f1
)
SELECT policy_id, state, fraud_score
FROM t
WHERE t.top_percentile_score <= 0.05
ORDER BY state, fraud_score DESC, policy_id
;


-- SQL Server
/* Write your T-SQL query statement below */
WITH t AS (
select f1.policy_id, f1.state, f1.fraud_score,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score) AS cnt_higher_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state) AS total_scores,
       convert(float, (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score)) /
       convert(float, (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state)) AS top_percentile_score
from fraud f1
)
SELECT policy_id, state, fraud_score
FROM t
WHERE t.top_percentile_score <= 0.05
ORDER BY state, fraud_score DESC, policy_id
;


# MySQL
# Write your MySQL query statement below
WITH t AS (
select f1.policy_id, f1.state, f1.fraud_score,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score) AS cnt_higher_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state) AS total_scores,
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state AND f2.fraud_score > f1.fraud_score) /
       (SELECT count(*) FROM fraud f2 WHERE f2.state = f1.state) AS top_percentile_score
from fraud f1
)
SELECT policy_id, state, fraud_score
FROM t
WHERE t.top_percentile_score <= 0.05
ORDER BY state, fraud_score DESC, policy_id
;


# Pandas
import pandas as pd

def top_percentile_fraud(fraud: pd.DataFrame) -> pd.DataFrame:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.quantile.html#pandas.core.groupby.DataFrameGroupBy.quantile
    # https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile
    # Group the data by state and calculate the top 5 percentile
    state_quantiles = fraud.groupby('state')['fraud_score'].quantile(0.95).reset_index(name='top_5_percentile')
    # Merge the percentiles back to the fraud DataFrame
    fraud = fraud.merge(state_quantiles, how='inner', on='state')
    # Trim the fraud DataFrame to the top 5 percentile data only
    fraud = fraud[fraud['fraud_score'] >= fraud['top_5_percentile']][['policy_id','state','fraud_score']]
    # Return data in the correct sorted order
    return fraud.sort_values(by=['state','fraud_score','policy_id'],ascending=[1,0,1])

