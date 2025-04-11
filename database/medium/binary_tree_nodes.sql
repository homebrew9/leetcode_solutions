-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:
    root = tree[tree['P'].isna()]['N']
    parent = tree[~tree['P'].isna()][['P']].drop_duplicates()['P']
    return pd.concat(
                     [
                        tree[tree['N'].isin(root)][['N']].assign(Type='Root'),
                        tree[(tree['N'].isin(parent)) & (~tree['N'].isin(root))][['N']].assign(Type='Inner'),
                        tree[(~tree['N'].isin(parent)) & (~tree['N'].isin(root))][['N']].assign(Type='Leaf')
                     ]
                    ).sort_values('N')

