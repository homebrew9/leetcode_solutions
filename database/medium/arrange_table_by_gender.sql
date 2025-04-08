-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
with t (user_id, gender, rn) as (
select user_id, gender,
       row_number() over (partition by gender order by user_id) as rn
from genders
),
t1 (user_id, gender, id) as (
select user_id, gender,
       case when gender = 'female'
            then
                case
                    when rn = 1 then 1
                    else 1 + (rn - 1) * 3
                end
            when gender = 'other'
            then
                case
                    when rn = 1 then 2
                    else 2 + (rn - 1) * 3
                end
            else
                case
                    when rn = 1 then 3
                    else 3 + (rn - 1) * 3
                end
       end as id
from t
)
select user_id, gender
from t1
order by id
;


# Pandas
import pandas as pd

def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    genders['rnk'] = ( genders
                      .sort_values(['gender','user_id'])
                      .groupby('gender', as_index=0)
                      .cumcount()+1
                     )
    genders['order'] = np.where(genders['gender'] == 'female', 1, np.where(genders['gender'] == 'other', 2, 3))
    return genders.sort_values(['rnk','order'])[['user_id', 'gender']]

