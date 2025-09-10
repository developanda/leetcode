import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    try:
        merge_data = pd.merge(units_sold, prices, how='right', on='product_id')
        merge_data = merge_data[(merge_data['purchase_date']<=merge_data['end_date'])&(merge_data['purchase_date']>=merge_data['start_date'])]
        merge_data['units'].fillna(0, inplace=True)

        result1 = merge_data.groupby(by='product_id').apply(lambda x: round((x['price']*x['units']).sum() / x['units'].sum(), 2) if x['units'].sum() != 0 else 0).reset_index()
        result1.columns = ['product_id', 'average_price']
        
        result = pd.DataFrame(columns=['product_id'])
        result['product_id'] = list(prices['product_id'].unique())

        result = pd.merge(result, result1, on='product_id', how = 'left')
        result['average_price'].fillna(0, inplace=True)
    except:
        result = pd.DataFrame(columns=['product_id', 'average_price'])
        result['product_id'] = list(prices['product_id'].unique())
        result['average_price'] = 0
    return result