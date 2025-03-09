-- Oracle
/* Write your PL/SQL query statement below */
with t (giver_id, receiver_id, gift_value, lvl, root_node, total_gift_value) as (
    select giver_id, receiver_id, gift_value, 1 as lvl, giver_id, gift_value as total_gift_value
      from SecretSanta
    union all
    select s.giver_id, s.receiver_id, s.gift_value, t.lvl+1, t.root_node, t.total_gift_value+s.gift_value
      from SecretSanta s
           inner join t on (t.receiver_id = s.giver_id)
     where s.giver_id <> t.root_node
),
t1 as (
    select distinct lvl as chain_length, total_gift_value
      from t
     where lvl = (select max(lvl) from t t1 where t1.root_node = t.root_node)
)
select row_number() over (order by chain_length desc, total_gift_value desc) as chain_id,
       chain_length, total_gift_value
  from t1
 order by chain_length desc, total_gift_value desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (giver_id, receiver_id, gift_value, lvl, root_node, total_gift_value) as (
    select giver_id, receiver_id, gift_value, 1 as lvl, giver_id, gift_value as total_gift_value
      from SecretSanta
    union all
    select s.giver_id, s.receiver_id, s.gift_value, t.lvl+1, t.root_node, t.total_gift_value+s.gift_value
      from SecretSanta s
           inner join t on (t.receiver_id = s.giver_id)
     where s.giver_id <> t.root_node
),
t1 as (
    select root_node, lvl, total_gift_value,
           max(lvl) over (partition by root_node) as max_level
      from t
),
t2 as (
    select distinct lvl as chain_length, total_gift_value
      from t1
     where lvl = max_level
)
select row_number() over (order by chain_length desc, total_gift_value desc) as chain_id,
       chain_length, total_gift_value
  from t2
order by chain_length desc, total_gift_value desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (giver_id, receiver_id, gift_value, lvl, root_node, total_gift_value) as (
    select giver_id, receiver_id, gift_value, 1 as lvl, giver_id, gift_value as total_gift_value
      from SecretSanta
    union all
    select s.giver_id, s.receiver_id, s.gift_value, t.lvl+1, t.root_node, t.total_gift_value+s.gift_value
      from SecretSanta s
           inner join t on (t.receiver_id = s.giver_id)
     where s.giver_id <> t.root_node
),
t1 as (
    select root_node, lvl, total_gift_value,
           max(lvl) over (partition by root_node) as max_level
      from t
),
t2 as (
    select distinct lvl as chain_length, total_gift_value
      from t1
     where lvl = max_level
)
select row_number() over (order by chain_length desc, total_gift_value desc) as chain_id,
       chain_length, total_gift_value
  from t2
order by chain_length desc, total_gift_value desc
;


# MySQL
# Write your MySQL query statement below
with recursive t (giver_id, receiver_id, gift_value, lvl, root_node, total_gift_value) as (
    select giver_id, receiver_id, gift_value, 1 as lvl, giver_id, gift_value as total_gift_value
      from SecretSanta
    union all
    select s.giver_id, s.receiver_id, s.gift_value, t.lvl+1, t.root_node, t.total_gift_value+s.gift_value
      from SecretSanta s
           inner join t on (t.receiver_id = s.giver_id)
     where s.giver_id <> t.root_node
),
t1 as (
    select root_node, lvl, total_gift_value,
           max(lvl) over (partition by root_node) as max_level
      from t
),
t2 as (
    select distinct lvl as chain_length, total_gift_value
      from t1
     where lvl = max_level
)
select row_number() over (order by chain_length desc, total_gift_value desc) as chain_id,
       chain_length, total_gift_value
  from t2
order by chain_length desc, total_gift_value desc
;


# Pandas
import pandas as pd

def find_gift_chains(secret_santa: pd.DataFrame) -> pd.DataFrame:
    def build_hierarchy(df_parent):
        global df_hier
        df_child = ( df_parent
                    .merge(secret_santa, how='inner', left_on='receiver_id', right_on='giver_id')
                    .query('giver_id_y != root_node')
                   )
        if len(df_child) == 0:
            return
        df_child = ( df_child
                    .assign(total_gift_value=df_child['total_gift_value']+df_child['gift_value_y'],
                            lvl=df_child['lvl']+1
                           )[['giver_id_y','receiver_id_y','gift_value_y','lvl','root_node','total_gift_value']]
                    .rename(columns={'giver_id_y':'giver_id','receiver_id_y':'receiver_id','gift_value_y':'gift_value'})
                   )
        df_hier = pd.concat([df_hier, df_child])
        df_parent = df_child
        build_hierarchy(df_parent)
    global df_hier
    df_hier = secret_santa.assign(lvl=1, root_node=secret_santa['giver_id'], total_gift_value=secret_santa['gift_value'])
    df_parent = df_hier
    build_hierarchy(df_parent)
    df = ( df_hier
          .groupby('root_node', as_index=0)
          .agg({'lvl':'max', 'total_gift_value':'max'})[['lvl','total_gift_value']]
          .drop_duplicates()
          .rename(columns={'lvl':'chain_length'})
          .sort_values(by=['chain_length','total_gift_value'],ascending=[0,0])
         )
    df['chain_id'] = df.reset_index().index + 1
    return df[['chain_id','chain_length','total_gift_value']]

