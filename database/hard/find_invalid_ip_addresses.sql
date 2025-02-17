-- Oracle
/* Write your PL/SQL query statement below */
select ip, count(*) as invalid_count
from logs
where regexp_count(ip, '[^.]+') != 4
or regexp_like(ip, '(^|\.)0')
or to_number(regexp_substr(ip, '[^.]+', 1, 1)) > 255
or to_number(regexp_substr(ip, '[^.]+', 1, 2)) > 255
or to_number(regexp_substr(ip, '[^.]+', 1, 3)) > 255
or to_number(regexp_substr(ip, '[^.]+', 1, 4)) > 255
group by ip
order by invalid_count desc, ip desc
;

-- PostgreSQL
-- Write your PostgreSQL query statement below
select ip, count(*) as invalid_count
from logs
where regexp_count(ip, '[^.]+') != 4
or regexp_like(ip, '(^|\.)0')
or regexp_substr(ip, '[^.]+', 1, 1)::int > 255
or regexp_substr(ip, '[^.]+', 1, 2)::int > 255
or regexp_substr(ip, '[^.]+', 1, 3)::int > 255
or regexp_substr(ip, '[^.]+', 1, 4)::int > 255
group by ip
order by invalid_count desc, ip desc
;

# MySQL
# Write your MySQL query statement below
select ip, count(*) as invalid_count
from logs
where length(ip) - length(replace(ip, '.', '')) != 3
or regexp_like(ip, '(^|\\.)0')
or cast(regexp_substr(ip, '[^.]+', 1, 1) as unsigned) > 255
or cast(regexp_substr(ip, '[^.]+', 1, 2) as unsigned) > 255
or cast(regexp_substr(ip, '[^.]+', 1, 3) as unsigned) > 255
or cast(regexp_substr(ip, '[^.]+', 1, 4) as unsigned) > 255
group by ip
order by invalid_count desc, ip desc
;

-- SQL Server
/* Write your T-SQL query statement below */
with t (log_id, ip) as (
select distinct log_id, ip
from logs
     cross apply string_split(ip, '.')
where len(ip) - len(replace(ip, '.', '')) <> 3
or ip like '0%'
or charindex('.0', ip) >= 1
or convert(int, value) > 255
)
select ip, count(*) as invalid_count
from t
group by ip
order by invalid_count desc, ip desc
;

# Pandas
import pandas as pd

def is_invalid(ip):
    arr = ip.split('.')
    return len(arr) != 4 or any([int(x) > 255 for x in arr]) or any([x.startswith('0') for x in arr])

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    logs['is_invalid'] = logs['ip'].apply(is_invalid)
    return ( logs[logs['is_invalid']][['ip','log_id']]
            .groupby('ip',as_index=0)['log_id']
            .count()
            .rename(columns={'log_id':'invalid_count'})
            .sort_values(by=['invalid_count','ip'], ascending=[False,False])
            )

