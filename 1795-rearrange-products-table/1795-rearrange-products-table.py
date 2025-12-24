import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # 1. Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.
    df = products.melt(
            # Column(s) you want to leave unchanged
            id_vars = ['product_id'],
            # Column(s) to unpivot. If not specified, uses all columns that are not set as id_vars, uncommented or commented we get the same result
            value_vars = ['store1', 'store2', 'store3'], 
            # Name to use for the ‘variable’ column. If None it uses frame.columns.name or ‘variable’.
            var_name = 'store',
            # This names the value column
            value_name = 'price'
            ).dropna() 
    return df