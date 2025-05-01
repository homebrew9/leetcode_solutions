-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    return products.pivot(values='price', index='product_id', columns='store').reset_index()

