import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['oe'] = 'odd_sum'
    transactions.loc[transactions['amount']%2==0, 'oe'] = 'even_sum'

    result = transactions.groupby(['transaction_date', 'oe'])['amount'].sum().reset_index()
    result = result.pivot_table(index='transaction_date', columns='oe', values='amount').reset_index()
    result = result.fillna(0)
    return result[['transaction_date','odd_sum','even_sum']]