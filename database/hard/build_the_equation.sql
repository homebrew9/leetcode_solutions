-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select power, factor,
       case when factor >= 0 then '+' || factor else to_char(factor) end as fmt_factor,
       case when power = 1 then 'X'
            when power = 0 then ''
            else 'X^'||power
       end as fmt_power,
       row_number() over (order by power desc) as rn
from terms
),
t1 as (
select rn, power, factor, fmt_factor, fmt_power, fmt_factor||fmt_power as single_term
from t
)
select listagg(single_term, '') within group (order by rn) || '=0' as equation
from t1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select power, factor,
       case when factor >= 0 then '+' || factor::text else factor::text end as fmt_factor,
       case when power = 1 then 'X'
            when power = 0 then ''
            else 'X^'||power::text
       end as fmt_power,
       row_number() over (order by power desc) as rn
from terms
),
t1 as (
select rn, power, factor, fmt_factor, fmt_power, fmt_factor||fmt_power as single_term
from t
)
select string_agg(single_term, '' order by rn) || '=0' as equation
from t1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select power, factor,
       case when factor >= 0 then '+' + convert(varchar,factor) else convert(varchar,factor) end as fmt_factor,
       case when power = 1 then 'X'
            when power = 0 then ''
            else 'X^' + convert(varchar,power)
       end as fmt_power,
       row_number() over (order by power desc) as rn
from terms
),
t1 as (
select rn, power, factor, fmt_factor, fmt_power, fmt_factor + fmt_power as single_term
from t
)
select string_agg(single_term, '') within group (order by rn) + '=0' as equation
from t1
;


# MySQL
# Write your MySQL query statement below
with t as (
select power, factor,
       case when factor >= 0 then concat('+', convert(factor, char))
            else convert(factor, char)
       end as fmt_factor,
       case when power = 1 then 'X'
            when power = 0 then ''
            else concat('X^', convert(power, char))
       end as fmt_power,
       row_number() over (order by power desc) as rn
from terms
),
t1 as (
select rn, power, factor, fmt_factor, fmt_power,
       concat(fmt_factor , fmt_power) as single_term
from t
)
select concat(group_concat(single_term order by rn separator ''), '=0') as equation
from t1
;


# Pandas
import pandas as pd

def build_the_equation(terms: pd.DataFrame) -> pd.DataFrame:
    terms.sort_values('power', ascending=False, inplace=True)
    terms['t'] = ( np.where(terms['factor']>0, '+', '') +
                   terms['factor'].astype(str) + 
                   np.where(terms['power']==0,
                            '',
                            np.where(terms['power']==1,
                                     'X',
                                     'X^' + terms['power'].astype(str)
                                    )
                           )
                 )
    terms['group_id'] = 0
    terms = terms.groupby('group_id',as_index=False)['t'].agg(lambda x: ''.join(x))
    eqn = terms['t'].item() + '=0'
    return pd.DataFrame(data={'equation': [eqn]})

