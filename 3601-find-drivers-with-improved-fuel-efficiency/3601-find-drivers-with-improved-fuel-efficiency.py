import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    # 1. calculation fuel efficiency for each trip
    trips['fuel_efficiency'] = trips['distance_km']/trips['fuel_consumed']

    # 2. separate date (first half, second half)
    trips.loc[trips['trip_date']<'2023-07-01', 'half'] = 'first_half'
    trips.loc[trips['trip_date']>='2023-07-01', 'half'] = 'second_half'

    # 3. select driver (include first & second)
    tmp_id_cnt = trips.groupby('driver_id')['half'].nunique().reset_index()
    driver_lst = list(tmp_id_cnt[tmp_id_cnt['half']==2]['driver_id'])
    print(driver_lst)

    # 4. calculate the efficiency improvement
    grp_half_efi = trips[trips['driver_id'].isin(driver_lst)].groupby(['driver_id', 'half'])['fuel_efficiency'].mean().reset_index()
    result = grp_half_efi.pivot_table(index='driver_id', columns='half', values='fuel_efficiency').reset_index()

    # 5. merge data
    f_result = result.merge(drivers, on='driver_id')

    # 6. calculate efficiency differnce
    f_result['efficiency_improvement'] = f_result['second_half'] - f_result['first_half']

    f_result['first_half_avg'] = round(f_result['first_half'], 2)
    f_result['second_half_avg'] = round(f_result['second_half'], 2)
    f_result['efficiency_improvement'] = round(f_result['efficiency_improvement'], 2)
    
    # 7. select driver (efficiency impoved)
    f_result = f_result[f_result['efficiency_improvement'] > 0]

    return f_result.sort_values(['efficiency_improvement', 'driver_name'], ascending=[False, True])[['driver_id', 'driver_name', 'first_half_avg', 'second_half_avg', 'efficiency_improvement']]