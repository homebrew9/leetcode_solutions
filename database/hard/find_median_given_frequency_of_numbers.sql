-- Oracle
/* Write your PL/SQL query statement below */
/*
0  4 1 4  6
1  4 5 8  6
2  3 9 11 6

0  7  1  7   6  7  0  0
1  1  8  8   6  7
2  3  9  11  6  7
3  1  12 12  6  7

0  6  1  6   6  7  0 
1  2  7  8   6  7     1
2  3  9  11  6  7
3  1  12 12  6  7

0  6  1  6   7  7
1  2  7  8   7  7  1
2  4  9  12  7  7
3  1  13 13  7  7

2  1  1  1 3 3
0  1  2  2 3 3
1  1  3  3 3 3
3  1  4  4 3 3
4  1  5  5 3 3
*/
--
with t (total) as (
select sum(frequency) as total
from numbers
),
t1 (median1_idx, median2_idx) as (
select case when mod(total, 2) = 1 then ceil(total/2) else total/2 end as median1_idx,
       case when mod(total, 2) = 1 then ceil(total/2) else total/2+1 end as median2_idx
from t
),
t2 (num, frequency, from_num, to_num, median1_idx, median2_idx) as (
select num, frequency,
       coalesce(sum(frequency) over (order by num rows between unbounded preceding and 1 preceding),0) + 1 as from_num,
       sum(frequency) over (order by num rows between unbounded preceding and current row) as to_num,
       t1.median1_idx, t1.median2_idx
from numbers
     cross join t1
),
t3 (num, frequency, from_num, to_num, median1_idx, median2_idx, median1, median2) as (
select num, frequency, from_num, to_num, median1_idx, median2_idx,
       case when median1_idx between from_num and to_num then num end as median1,
       case when median2_idx between from_num and to_num then num end as median2
from t2
)
select (max(median1) + max(median2))/2 as median
from t3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (total) as (
select sum(frequency) as total
from numbers
),
t1 (median1_idx, median2_idx) as (
select case when mod(total, 2) = 1 then ceil(total::numeric/2) else total::numeric/2 end as median1_idx,
       case when mod(total, 2) = 1 then ceil(total::numeric/2) else total::numeric/2+1 end as median2_idx
from t
),
t2 (num, frequency, from_num, to_num, median1_idx, median2_idx) as (
select num, frequency,
       coalesce(sum(frequency) over (order by num rows between unbounded preceding and 1 preceding),0) + 1 as from_num,
       sum(frequency) over (order by num rows between unbounded preceding and current row) as to_num,
       t1.median1_idx, t1.median2_idx
from numbers
     cross join t1
--order by num
)
--select * from t2;
--/*
,
t3 (num, frequency, from_num, to_num, median1_idx, median2_idx, median1, median2) as (
select num, frequency, from_num, to_num, median1_idx, median2_idx,
       case when median1_idx between from_num and to_num then num end as median1,
       case when median2_idx between from_num and to_num then num end as median2
from t2
)
select (max(median1) + max(median2))::numeric/2 as median
from t3
;
--*/


-- SQL Server
/* Write your T-SQL query statement below */
with t (total) as (
select sum(frequency) as total
from numbers
),
t1 (median1_idx, median2_idx) as (
select case when total % 2 = 1 then ceiling(convert(float, total)/2) else convert(float, total)/2 end as median1_idx,
       case when total % 2 = 1 then ceiling(convert(float, total)/2) else convert(float, total)/2+1 end as median2_idx
from t
),
t2 (num, frequency, from_num, to_num, median1_idx, median2_idx) as (
select num, frequency,
       coalesce(sum(frequency) over (order by num rows between unbounded preceding and 1 preceding),0) + 1 as from_num,
       sum(frequency) over (order by num rows between unbounded preceding and current row) as to_num,
       t1.median1_idx, t1.median2_idx
from numbers
     cross join t1
),
t3 (num, frequency, from_num, to_num, median1_idx, median2_idx, median1, median2) as (
select num, frequency, from_num, to_num, median1_idx, median2_idx,
       case when median1_idx between from_num and to_num then num end as median1,
       case when median2_idx between from_num and to_num then num end as median2
from t2
)
select convert(float, (max(median1) + max(median2))) / 2 as median
from t3
;


# MySQL
# Write your MySQL query statement below
--
with t (total) as (
select sum(frequency) as total
from numbers
),
t1 (median1_idx, median2_idx) as (
select case when mod(total, 2) = 1 then ceil(total/2) else total/2 end as median1_idx,
       case when mod(total, 2) = 1 then ceil(total/2) else total/2+1 end as median2_idx
from t
),
t2 (num, frequency, from_num, to_num, median1_idx, median2_idx) as (
select num, frequency,
       coalesce(sum(frequency) over (order by num rows between unbounded preceding and 1 preceding),0) + 1 as from_num,
       sum(frequency) over (order by num rows between unbounded preceding and current row) as to_num,
       t1.median1_idx, t1.median2_idx
from numbers
     cross join t1
),
t3 (num, frequency, from_num, to_num, median1_idx, median2_idx, median1, median2) as (
select num, frequency, from_num, to_num, median1_idx, median2_idx,
       case when median1_idx between from_num and to_num then num end as median1,
       case when median2_idx between from_num and to_num then num end as median2
from t2
)
select (max(median1) + max(median2))/2 as median
from t3
;


# Pandas
import pandas as pd

def median_frequency(numbers: pd.DataFrame) -> pd.DataFrame:
    numbers.sort_values('num', inplace=True)
    numbers['to_num'] = numbers['frequency'].cumsum()
    numbers['from_num'] = numbers.shift(1).fillna(0)['to_num'].astype(int)+1
    total = numbers['frequency'].sum()
    numbers['median1_idx'] = total/2+0.5 if total%2==1 else total//2
    numbers['median2_idx'] = total/2+0.5 if total%2==1 else total//2+1
    median1 = numbers.query('from_num <= median1_idx & median1_idx <= to_num')['num'].item()
    median2 = numbers.query('from_num <= median2_idx & median2_idx <= to_num')['num'].item()
    return pd.DataFrame(data={'median': [(median1 + median2)/2]})

