import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    merge_purchases = product_purchases.merge(product_purchases, on='user_id')
    merge_purchases = merge_purchases[merge_purchases['product_id_x'] < merge_purchases['product_id_y']][['user_id','product_id_x','product_id_y']]


    result = merge_purchases.groupby(['product_id_x','product_id_y'])['user_id'].count().reset_index()
    result = result[result['user_id']>=3]


    result = result.merge(product_info[['product_id','category']], left_on = 'product_id_x', right_on='product_id', how='left')
    result.drop('product_id', axis=1, inplace=True)

    product_info = product_info.rename(columns={'category':'category_y'})
    result = result.merge(product_info[['product_id','category_y']], left_on = 'product_id_y', right_on='product_id', how='left')
    result.drop('product_id', axis=1, inplace=True)

    result = result.rename(columns={'product_id_x':'product1_id','product_id_y':'product2_id','category':'product1_category','category_y':'product2_category','user_id':'customer_count'})

    return result[['product1_id','product2_id','product1_category','product2_category','customer_count']].sort_values(['customer_count','product1_id', 'product2_id'], ascending=[False, True, True])