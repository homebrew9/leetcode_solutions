-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, how='inner', on='product_id')
    df['spending'] = df['quantity']*df['price']
    return (  df.groupby('user_id', as_index=False)['spending']
                .sum()[['user_id','spending']]
                .sort_values(by=['spending','user_id'], ascending=[False,True])
           )

