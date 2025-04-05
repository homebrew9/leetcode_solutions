-- Oracle
/* Write your PL/SQL query statement below */
--
WITH t AS (
    SELECT q1.person_name, q1.turn, sum(q2.weight) AS cumulative_weight
    FROM queue q1 INNER JOIN queue q2 ON (q2.turn <= q1.turn)
    GROUP BY q1.person_name, q1.turn
    HAVING sum(q2.weight) <= 1000
    ORDER BY q1.turn DESC
)
SELECT person_name FROM t WHERE rownum = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
WITH t AS (
    SELECT q1.person_name, q1.turn, sum(q2.weight) AS cumulative_weight
    FROM queue q1 INNER JOIN queue q2 ON (q2.turn <= q1.turn)
    GROUP BY q1.person_name, q1.turn
    HAVING sum(q2.weight) <= 1000
    ORDER BY q1.turn DESC
)
SELECT person_name FROM t limit 1
;


-- SQL Server
/* Write your T-SQL query statement below */
WITH t AS (
    SELECT q1.person_name, q1.turn, sum(q2.weight) AS cumulative_weight
    FROM queue q1 INNER JOIN queue q2 ON (q2.turn <= q1.turn)
    GROUP BY q1.person_name, q1.turn
    HAVING sum(q2.weight) <= 1000
    --ORDER BY q1.turn DESC
)
SELECT TOP 1 person_name FROM t
ORDER BY turn DESC
;


# MySQL
# Write your MySQL query statement below
WITH t AS (
    SELECT q1.person_name, q1.turn, sum(q2.weight) AS cumulative_weight
    FROM queue q1 INNER JOIN queue q2 ON (q2.turn <= q1.turn)
    GROUP BY q1.person_name, q1.turn
    HAVING sum(q2.weight) <= 1000
    ORDER BY q1.turn DESC
)
SELECT person_name FROM t LIMIT 1
;


# Pandas
import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    return ( queue
            .assign(cumulative_weight=queue.sort_values('turn')['weight'].cumsum())
            .query('cumulative_weight <= 1000')
            .sort_values('turn')
            .tail(1)[['person_name']]
           )

