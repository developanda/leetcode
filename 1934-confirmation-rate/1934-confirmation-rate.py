import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    m_data = pd.DataFrame(signups['user_id']).merge(confirmations, on='user_id', how='left')
    m_data['action_cnt']=0
    m_data.loc[m_data['action'] == 'confirmed', 'action_cnt']=1
    
    result = m_data.groupby('user_id')['action_cnt'].agg([len, sum]).reset_index()
    result['confirmation_rate'] = round(result['sum']/result['len'],2)
    
    return result[['user_id','confirmation_rate']]