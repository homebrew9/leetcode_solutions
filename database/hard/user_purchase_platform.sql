-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select s1.user_id, s1.spend_date, s1.platform, s1.amount,
           case when s2.platform is not null then 'both' else s1.platform end as platform_upd
      from spending s1
           left outer join spending s2 on (s2.user_id = s1.user_id and
                                           s2.spend_date = s1.spend_date and
                                           s2.platform != s1.platform
                                          )
),
t1 as (
    select user_id, spend_date, platform_upd as platform, sum(amount) as total_amount
      from t
     group by user_id, spend_date, platform_upd
),
t2 as (
    select spend_date, platform, sum(total_amount) as total_amount, count(user_id) as total_users
      from t1
     group by spend_date, platform
),
template as (
    select x.spend_date, y.platform
      from (select distinct spend_date from spending) x
           cross join (select 'desktop' as platform from dual union all
                       select 'mobile' from dual union all
                       select 'both' from dual
                      ) y
)
select to_char(tmp.spend_date, 'yyyy-mm-dd') as spend_date, tmp.platform,
       coalesce(t2.total_amount, 0) as total_amount,
       coalesce(t2.total_users, 0) as total_users
  from template tmp
       left outer join t2 on (t2.spend_date = tmp.spend_date and t2.platform = tmp.platform)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select s1.user_id, s1.spend_date, s1.platform, s1.amount,
           case when s2.platform is not null then 'both' else s1.platform end as platform_upd
      from spending s1
           left outer join spending s2 on (s2.user_id = s1.user_id and
                                           s2.spend_date = s1.spend_date and
                                           s2.platform != s1.platform
                                          )
),
t1 as (
    select user_id, spend_date, platform_upd as platform, sum(amount) as total_amount
      from t
     group by user_id, spend_date, platform_upd
),
t2 as (
    select spend_date, platform, sum(total_amount) as total_amount, count(user_id) as total_users
      from t1
     group by spend_date, platform
),
template as (
    select x.spend_date, y.platform
      from (select distinct spend_date from spending) x
           cross join (select 'desktop' as platform union all
                       select 'mobile' union all
                       select 'both'
                      ) y
)
select to_char(tmp.spend_date, 'yyyy-mm-dd') as spend_date, tmp.platform,
       coalesce(t2.total_amount, 0) as total_amount,
       coalesce(t2.total_users, 0) as total_users
  from template tmp
       left outer join t2 on (t2.spend_date = tmp.spend_date and t2.platform = tmp.platform)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select s1.user_id, s1.spend_date, s1.platform, s1.amount,
           case when s2.platform is not null then 'both' else s1.platform end as platform_upd
      from spending s1
           left outer join spending s2 on (s2.user_id = s1.user_id and
                                           s2.spend_date = s1.spend_date and
                                           s2.platform != s1.platform
                                          )
),
t1 as (
    select user_id, spend_date, platform_upd as platform, sum(amount) as total_amount
      from t
     group by user_id, spend_date, platform_upd
),
t2 as (
    select spend_date, platform, sum(total_amount) as total_amount, count(user_id) as total_users
      from t1
     group by spend_date, platform
),
template as (
    select x.spend_date, y.platform
      from (select distinct spend_date from spending) x
           cross join (select 'desktop' as platform union all
                       select 'mobile' union all
                       select 'both'
                      ) y
)
select tmp.spend_date, tmp.platform,
       coalesce(t2.total_amount, 0) as total_amount,
       coalesce(t2.total_users, 0) as total_users
  from template tmp
       left outer join t2 on (t2.spend_date = tmp.spend_date and t2.platform = tmp.platform)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select s1.user_id, s1.spend_date, s1.platform, s1.amount,
           case when s2.platform is not null then 'both' else s1.platform end as platform_upd
      from spending s1
           left outer join spending s2 on (s2.user_id = s1.user_id and
                                           s2.spend_date = s1.spend_date and
                                           s2.platform != s1.platform
                                          )
),
t1 as (
    select user_id, spend_date, platform_upd as platform, sum(amount) as total_amount
      from t
     group by user_id, spend_date, platform_upd
),
t2 as (
    select spend_date, platform, sum(total_amount) as total_amount, count(user_id) as total_users
      from t1
     group by spend_date, platform
),
template as (
    select x.spend_date, y.platform
      from (select distinct spend_date from spending) x
           cross join (select 'desktop' as platform union all
                       select 'mobile' union all
                       select 'both'
                      ) y
)
select tmp.spend_date, tmp.platform,
       coalesce(t2.total_amount, 0) as total_amount,
       coalesce(t2.total_users, 0) as total_users
  from template tmp
       left outer join t2 on (t2.spend_date = tmp.spend_date and t2.platform = tmp.platform)
;


# Pandas
import pandas as pd

def user_purchase(spending: pd.DataFrame) -> pd.DataFrame:
    df = spending.groupby(['user_id','spend_date'],as_index=0)['platform'].count()
    df['ptype'] = np.where(df['platform']>1, 'both', '')
    df.drop(columns='platform', inplace=True)
    df1 = spending.merge(df, how='left', on=['user_id','spend_date'])
    df1['platform'] = np.where(df1['ptype']=='', df1['platform'], df1['ptype'])
    df1 = df1.groupby(['user_id','spend_date','platform'],as_index=0)['amount'].sum()
    df1 = df1.groupby(['spend_date','platform'],as_index=0).agg({'amount': 'sum', 'user_id': 'count'})
    template = spending[['spend_date']].drop_duplicates().merge(
        pd.DataFrame(data={'platform': ['desktop','mobile','both']}),
        how='cross'
    )
    return ( template
            .merge(df1, how='left', on=['spend_date','platform'])
            .fillna(0)
            .rename(columns={'amount': 'total_amount', 'user_id': 'total_users'})
           )

