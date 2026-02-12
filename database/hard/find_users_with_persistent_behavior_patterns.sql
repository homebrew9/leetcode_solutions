-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, action_date, action, marker) as (
    select user_id, TO_CHAR(action_date, 'YYYY-MM-DD') as action_date, action,
           case when action_date = lag(action_date) over (partition by user_id order by action_date) + 1 and
                    action = lag(action) over (partition by user_id order by action_date)
                then 0
                else 1
           end as marker
    from activity
),
t1 (user_id, action_date, action, marker, group_id) as (
    select user_id, action_date, action, marker,
        sum(marker) over (partition by user_id
                          order by action_date rows between unbounded preceding and current row) as group_id
    from t
),
t2 (user_id, action, streak_length, start_date, end_date) as (
    select user_id, action,
           count(*) as streak_length,
           min(action_date) as start_date, max(action_date) as end_date
    from t1
    group by user_id, action, group_id
    having count(*) >= 5
)
select x.user_id, x.action, x.streak_length, x.start_date, x.end_date
  from t2 x
 where x.streak_length = (
                           select max(y.streak_length)
                             from t2 y
                            where y.user_id = x.user_id
                              and y.action = x.action
                         )
 order by x.streak_length desc, x.user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, action_date, action, marker) as (
    select user_id, TO_CHAR(action_date, 'YYYY-MM-DD') as action_date, action,
           case when action_date = lag(action_date) over (partition by user_id order by action_date) + INTERVAL '1' DAY
                     and action = lag(action) over (partition by user_id order by action_date)
                then 0
                else 1
           end as marker
    from activity
),
t1 (user_id, action_date, action, marker, group_id) as (
    select user_id, action_date, action, marker,
        sum(marker) over (partition by user_id
                          order by action_date rows between unbounded preceding and current row) as group_id
    from t
),
t2 (user_id, action, streak_length, start_date, end_date) as (
    select user_id, action,
           count(*) as streak_length,
           min(action_date) as start_date, max(action_date) as end_date
    from t1
    group by user_id, action, group_id
    having count(*) >= 5
)
select x.user_id, x.action, x.streak_length, x.start_date, x.end_date
  from t2 x
 where x.streak_length = (
                           select max(y.streak_length)
                             from t2 y
                            where y.user_id = x.user_id
                              and y.action = x.action
                         )
 order by x.streak_length desc, x.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, action_date, action, marker) as (
    select user_id, action_date, action,
           case when action_date = DATEADD(DAY, 1, lag(action_date) over (partition by user_id order by action_date))
                     and action = lag(action) over (partition by user_id order by action_date)
                then 0
                else 1
           end as marker
    from activity
),
t1 (user_id, action_date, action, marker, group_id) as (
    select user_id, action_date, action, marker,
        sum(marker) over (partition by user_id
                          order by action_date rows between unbounded preceding and current row) as group_id
    from t
),
t2 (user_id, action, streak_length, start_date, end_date) as (
    select user_id, action,
           count(*) as streak_length,
           min(action_date) as start_date, max(action_date) as end_date
    from t1
    group by user_id, action, group_id
    having count(*) >= 5
)
select x.user_id, x.action, x.streak_length, x.start_date, x.end_date
  from t2 x
 where x.streak_length = (
                           select max(y.streak_length)
                             from t2 y
                            where y.user_id = x.user_id
                              and y.action = x.action
                         )
 order by x.streak_length desc, x.user_id
;


# MySQL
# Write your MySQL query statement below
with t (user_id, action_date, action, marker) as (
    select user_id, action_date, action,
           case when action_date = lag(action_date) over (partition by user_id order by action_date) + INTERVAL '1' DAY
                and action = lag(action) over (partition by user_id order by action_date)
                then 0
                else 1
           end as marker
    from activity
),
t1 (user_id, action_date, action, marker, group_id) as (
    select user_id, action_date, action, marker,
        sum(marker) over (partition by user_id
                          order by action_date rows between unbounded preceding and current row) as group_id
    from t
),
t2 (user_id, action, streak_length, start_date, end_date) as (
    select user_id, action,
           count(*) as streak_length,
           min(action_date) as start_date, max(action_date) as end_date
    from t1
    group by user_id, action, group_id
    having count(*) >= 5
)
select x.user_id, x.action, x.streak_length, x.start_date, x.end_date
  from t2 x
 where x.streak_length = (
                           select max(y.streak_length)
                             from t2 y
                            where y.user_id = x.user_id
                              and y.action = x.action
                         )
 order by x.streak_length desc, x.user_id
;


# Pandas
import pandas as pd

def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    activity['action_date'] = pd.to_datetime(activity['action_date'])
    activity.sort_values(by=['user_id','action_date'], ascending=[True,True], inplace=True)
    activity['marker'] = ( np.where(
                               (activity['user_id'] == activity['user_id'].shift(1)) &
                               (activity['action_date'] == activity['action_date'].shift(1) + pd.Timedelta(days=1)) &
                               (activity['action'] == activity['action'].shift(1)),
                               0,
                               1
                           )
                        )
    activity['group_id'] = activity.groupby('user_id', as_index=0)['marker'].cumsum()
    df = ( activity
          .groupby(['user_id','action','group_id'], as_index=0)
          .agg(streak_length=('action_date','count'),start_date=('action_date','min'),end_date=('action_date','max'))
          .query('streak_length >= 5')
         )
    df['drnk'] = ( df
                  .groupby('user_id', as_index=0)['streak_length']
                  .rank(method='dense', ascending=False)
                 )
    df1 = ( df
           .query('drnk == 1')[['user_id','action','streak_length','start_date','end_date']]
           .sort_values(by=['streak_length','user_id'], ascending=[False,True])
          )
    return df1














