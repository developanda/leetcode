import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    result['product_id'] = list(products['product_id'].unique())
    
    temp = products[products['change_date']<='2019-08-16'].sort_values('change_date').drop_duplicates(subset='product_id', keep='last')
    result = result.merge(temp, on='product_id', how='left')
    result['price'] = result['new_price'].fillna(10)

    return result[['product_id', 'price']]