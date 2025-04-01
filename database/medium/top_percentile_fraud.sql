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


# Pandas

