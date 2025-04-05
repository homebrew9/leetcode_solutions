-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_count = len(product)
    return ( customer
            .drop_duplicates()
            .groupby('customer_id', as_index=0)['product_key']
            .count()
            .query('product_key == @product_count')[['customer_id']]
           )

