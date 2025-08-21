import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    den = len(df:= delivery.groupby("customer_id").min())                       #  <-- 1

    num = len(df[df.order_date == df.customer_pref_delivery_date])             #  <-- 2

    return pd.DataFrame({"immediate_percentage": [num / den *100]}).round(2)   #  <-- 3

    result = pd.DataFrame(columns={'immediate_percentage':[percent_value]})
    return delivery