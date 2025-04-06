-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['parity'] = np.where(transactions['amount'] % 2 == 1, 'odd_sum', 'even_sum')
    df = transactions.groupby(['transaction_date', 'parity'], as_index=0)['amount'].sum()
    return ( df
            .pivot(columns='parity', values='amount', index='transaction_date')
            .reset_index()
            .fillna(0)[['transaction_date', 'odd_sum', 'even_sum']]
            .sort_values('transaction_date')
           )

