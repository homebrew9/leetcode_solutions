-- Oracle
/* Write your PL/SQL query statement below */
select m.member_id, m.name,
       case when count(v.visit_id) = 0 then 'Bronze'
            when 100 * count(p.charged_amount) / count(v.visit_id) >= 80 then 'Diamond'
            when 100 * count(p.charged_amount) / count(v.visit_id) >= 50 then 'Gold'
            else 'Silver'
       end as category
from members m
     left outer join visits v on (v.member_id = m.member_id)
     left outer join purchases p on (p.visit_id = v.visit_id)
group by m.member_id, m.name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select m.member_id, m.name,
       case when count(v.visit_id) = 0 then 'Bronze'
            when 100 * count(p.charged_amount)::numeric / count(v.visit_id)::numeric >= 80 then 'Diamond'
            when 100 * count(p.charged_amount)::numeric / count(v.visit_id)::numeric >= 50 then 'Gold'
            else 'Silver'
       end as category
from members m
     left outer join visits v on (v.member_id = m.member_id)
     left outer join purchases p on (p.visit_id = v.visit_id)
group by m.member_id, m.name
;


-- SQL Server
/* Write your T-SQL query statement below */
select m.member_id, m.name,
       case when count(v.visit_id) = 0 then 'Bronze'
            when 100 * convert(float, count(p.charged_amount)) / convert(float, count(v.visit_id)) >= 80 then 'Diamond'
            when 100 * convert(float, count(p.charged_amount)) / convert(float, count(v.visit_id)) >= 50 then 'Gold'
            else 'Silver'
       end as category
from members m
     left outer join visits v on (v.member_id = m.member_id)
     left outer join purchases p on (p.visit_id = v.visit_id)
group by m.member_id, m.name
;


# MySQL
# Write your MySQL query statement below
select m.member_id, m.name,
       case when count(v.visit_id) = 0 then 'Bronze'
            when 100 * count(p.charged_amount) / count(v.visit_id) >= 80 then 'Diamond'
            when 100 * count(p.charged_amount) / count(v.visit_id) >= 50 then 'Gold'
            else 'Silver'
       end as category
from members m
     left outer join visits v on (v.member_id = m.member_id)
     left outer join purchases p on (p.visit_id = v.visit_id)
group by m.member_id, m.name
;


# Pandas
import pandas as pd

def find_categories(members: pd.DataFrame, visits: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    df = ( members
          .merge(visits, how='left', on='member_id')
          .merge(purchases, how='left', on='visit_id')
         )
    df = ( df
          .groupby(['member_id','name'], as_index=False)
          .agg(visit_count=('visit_id','count'), purchase_count=('charged_amount','count'))
         )
    df['category'] = np.where(
                         df['visit_count'] == 0,
                         'Bronze',
                         np.where(
                             100 * df['purchase_count'] / df['visit_count'] >= 80,
                             'Diamond',
                             np.where (
                                 100 * df['purchase_count'] / df['visit_count'] >= 50,
                                 'Gold',
                                 'Silver'
                             )
                         )
                     )
    return df[['member_id','name','category']]

