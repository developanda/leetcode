import pandas as pd

def find_category_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    df = product_purchases.assign(category=product_purchases['product_id'].map(product_info.set_index('product_id').category))
    df = df.merge(df, on='user_id')
    df = df.drop_duplicates(['user_id', 'category_x', 'category_y'])
    pairs = Counter(zip(df['category_x'],df['category_y']))
    data = [(c1, c2, cnt) for ((c1, c2), cnt) in pairs.items() if c1 < c2 and cnt > 2]
    return pd.DataFrame(data, columns=['category1', 'category2', 'customer_count']).sort_values(['customer_count', 'category1', 'category2'], ascending=[0, 1, 1])