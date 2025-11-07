import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['amount'].fillna(0)
    merge_data = visits.merge(transactions, on='visit_id', how='left')
    extrac_data = merge_data[merge_data['amount'].isnull()].groupby('customer_id')['visit_id'].agg({'min','count'}).reset_index()
    result = extrac_data.rename(columns={'customer_id':'customer_id', 'min': 'id', 'count': 'count_no_trans'})
    return result.sort_values('id', ascending=True)[['customer_id','count_no_trans']]