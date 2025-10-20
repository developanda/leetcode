import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['oper_by'] = 1
    stocks.loc[stocks['operation']=='Buy','oper_by'] = -1

    stocks['capital_gain_loss'] = stocks['oper_by']*stocks['price']
    result = stocks.groupby('stock_name')['capital_gain_loss'].sum().reset_index()
    return result