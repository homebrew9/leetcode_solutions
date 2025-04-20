-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    df1 = (  ads[ads['action']=='Clicked']
             .groupby('ad_id',as_index=False)['action']
             .count()
             .rename(columns={'action':'clicked'})
          )
    df2 = (  ads[ads['action']!='Ignored']
             .groupby('ad_id',as_index=False)['action']
             .count()
             .rename(columns={'action':'total'})
          )
    df = pd.merge(df1, df2, how='inner', on='ad_id')
    df['ctr'] = round(df['clicked']/df['total']*100, 2)
    df = df[['ad_id', 'ctr']]
    return (  ads[['ad_id']]
              .drop_duplicates()
              .merge(df, how='left')
              .fillna(0.00)
              .sort_values(by=['ctr','ad_id'],ascending=[False,True])
           )

