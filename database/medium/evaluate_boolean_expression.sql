-- Oracle
/* Write your PL/SQL query statement below */
select e.left_operand, e.operator, e.right_operand,
       case when e.operator = '>'
            then case when vl.value > vr.value then 'true' else 'false' end
            when e.operator = '<'
            then case when vl.value < vr.value then 'true' else 'false' end
            when e.operator = '='
            then case when vl.value = vr.value then 'true' else 'false' end
       end as value
  from expressions e
       inner join variables vl on (vl.name = e.left_operand)
       inner join variables vr on (vr.name = e.right_operand)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e.left_operand, e.operator, e.right_operand,
       case when e.operator = '>' then (vl.value > vr.value)::text
            when e.operator = '<' then (vl.value < vr.value)::text
            when e.operator = '=' then (vl.value = vr.value)::text
       end as value
  from expressions e
       inner join variables vl on (vl.name = e.left_operand)
       inner join variables vr on (vr.name = e.right_operand)
;


-- SQL Server
/* Write your T-SQL query statement below */
select e.left_operand, e.operator, e.right_operand,
       case e.operator
           when '>' then case when v1.value > v2.value then 'true' else 'false' end
           when '<' then case when v1.value < v2.value then 'true' else 'false' end
           when '=' then case when v1.value = v2.value then 'true' else 'false' end
       end as value
from expressions e
     inner join variables v1 on (v1.name = e.left_operand)
     inner join variables v2 on (v2.name = e.right_operand)
;


# MySQL
# Write your MySQL query statement below
select e.left_operand, e.operator, e.right_operand,
       case e.operator
           when '>' then case when v1.value > v2.value then 'true' else 'false' end
           when '<' then case when v1.value < v2.value then 'true' else 'false' end
           when '=' then case when v1.value = v2.value then 'true' else 'false' end
       end as value
from expressions e
     inner join variables v1 on (v1.name = e.left_operand)
     inner join variables v2 on (v2.name = e.right_operand)
;       


# Pandas
import pandas as pd

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    df = ( expressions
          .merge(variables, how='inner', left_on='left_operand', right_on='name')
          .merge(variables, how='inner', left_on='right_operand', right_on='name')
         )
    df['value'] = ( np.where(
                        df['operator'] == '>',
                        df['value_x'] > df['value_y'],
                        np.where(
                            df['operator'] == '<',
                            df['value_x'] < df['value_y'],
                            np.where(
                                df['operator'] == '=',
                                df['value_x'] == df['value_y'],
                                ''
                            )
                        )
                    )
                  )
    df = ( df[['left_operand','operator','right_operand','value']]
          .replace({True: 'true', False: 'false'})
         )
    return df

