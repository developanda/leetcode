import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id','make_name'])[['lead_id','partner_id']].nunique().reset_index()
    result.columns = ['date_id','make_name','unique_leads','unique_partners']
    return result.sort_values(['date_id','make_name'], ascending=True)