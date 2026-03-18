import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:

    pattern = r'\bSN\d{4}-\d{4}\b'
    
    return products[
        products['description'].str.contains(pattern, na=False)
    ].sort_values('product_id')