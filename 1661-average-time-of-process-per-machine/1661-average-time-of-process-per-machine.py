import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    data_a = activity[activity['activity_type']=='start'][['machine_id','process_id', 'timestamp']]
    data_a = data_a.rename(columns={'timestamp':'start_time'})
    data_b = activity[activity['activity_type']=='end'][['machine_id','process_id', 'timestamp']]
    data_b = data_b.rename(columns={'timestamp':'end_time'})

    merge_data = data_a.merge(data_b, on=['machine_id', 'process_id'])

    merge_data['processing_time'] = merge_data['end_time']-merge_data['start_time']
    result = merge_data.groupby('machine_id')['processing_time'].mean().round(3).reset_index()

    return result
    