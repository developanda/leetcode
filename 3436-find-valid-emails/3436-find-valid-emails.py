import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users['email_part1'] = users['email'].str.split('@').str[0]
    users['email_part2'] = users['email'].str.split('@').str[1]
    users['email_part3'] = users['email_part2'].str.split('.').str[1]
    users['email_part2'] = users['email_part2'].str.split('.').str[0]

    users['email_part1'].replace('_','')

    return users[(users['email'].str.contains('@'))
                  &(users['email_part3'] == 'com')
                  &(users['email_part1'].str.isalnum())
                  &(users['email_part2'].str.isalpha())].sort_values('user_id')[['user_id','email']]