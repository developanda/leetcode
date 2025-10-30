import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        activities.groupby('sell_date')['product']
        .apply(lambda x: sorted(x.unique()))
        .reset_index()
    )
    grouped['num_sold'] = grouped['product'].apply(len)
    grouped['products'] = grouped['product'].apply(lambda x: ','.join(x))
    grouped = grouped[['sell_date', 'num_sold', 'products']].sort_values('sell_date')
    return grouped