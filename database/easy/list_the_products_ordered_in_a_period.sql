-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return ( orders[orders['order_date'].dt.strftime('%Y-%m') == '2020-02']
            .groupby('product_id', as_index=0)['unit']
            .sum()
            .query('unit >= 100')
            .merge(products, how='inner', on='product_id')[['product_name', 'unit']]
           )

