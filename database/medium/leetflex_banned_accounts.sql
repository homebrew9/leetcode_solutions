-- Oracle
/* Write your PL/SQL query statement below */
select distinct x.account_id
  from LogInfo x
 where exists (select null
                 from LogInfo y
                where y.account_id = x.account_id
                  and y.ip_address != x.ip_address
                  and x.login between y.login and y.logout
              )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct x.account_id
  from LogInfo x
 where exists (select null
                 from LogInfo y
                where y.account_id = x.account_id
                  and y.ip_address != x.ip_address
                  and x.login between y.login and y.logout
              )
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct x.account_id
  from LogInfo x
 where exists (select null
                 from LogInfo y
                where y.account_id = x.account_id
                  and y.ip_address != x.ip_address
                  and x.login between y.login and y.logout
              )
;


# MySQL
# Write your MySQL query statement below
select distinct x.account_id
  from LogInfo x
 where exists (select null
                 from LogInfo y
                where y.account_id = x.account_id
                  and y.ip_address != x.ip_address
                  and x.login between y.login and y.logout
              )
;


# Pandas
import pandas as pd

def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    return ( log_info
            .merge(log_info, how='inner', on='account_id')
            .query('ip_address_x != ip_address_y and  \
                   (login_x <= login_y <= logout_x or \
                    login_y <= login_x <= logout_y    \
                   )'
                  )[['account_id']]
            .drop_duplicates()
           )

