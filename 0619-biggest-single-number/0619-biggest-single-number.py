import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    df = my_numbers.groupby('num').size().reset_index(name='count')
    singles = df[df['count']==1]['num']
    return pd.DataFrame({'num':[singles.max()]})