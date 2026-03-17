import pandas as pd
# Return true in case the ip address
# is invalid
def is_invalid_address(ip):
    segment_split = ip.split('.')
    
    if len(segment_split) != 4:
        return True

    for segment in segment_split:
        if segment.startswith('0'):
            return True
        segment_int = int(segment)
        if segment_int > 255:
            return True    
    return False
        
def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    logs['is_invalid'] = logs['ip'].apply(is_invalid_address)

    logs = logs[logs['is_invalid']][['log_id','ip']]

    result = logs.groupby('ip', as_index=False).agg(
        invalid_count=('log_id', 'count'))

    result = result.sort_values(
        by=['invalid_count', 'ip'],
        ascending=[False, False]
    )
    
    return result