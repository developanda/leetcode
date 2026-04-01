import pandas as pd

def seasonal_sales_analysis(products: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    # make season column
    season_map = {
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Fall', 10: 'Fall', 11: 'Fall'
    }

    # Apply mapping
    sales['season'] = sales['sale_date'].dt.month.map(season_map)
    # Merge data
    merge_df = sales.merge(products, on='product_id', how='left')

    # make revenue
    merge_df['revenue'] = merge_df['quantity'] * merge_df['price']

    # quantity, revenue by season
    result = merge_df.groupby(['season', 'category'])[['quantity', 'revenue']].sum().reset_index()
    print(result)
    result = result.sort_values(['season', 'quantity', 'revenue'], ascending=[True, False, False]).drop_duplicates('season', keep='first')
    result = result.rename(columns={'quantity':'total_quantity', 'revenue': 'total_revenue'})

    return result