import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # 이메일 패턴: 영문자로 시작 + 영문자/숫자/._-만 포함 + @leetcode.com으로 끝
    pattern = r'^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'
    
    # 정규식 조건에 맞는 행만 필터링
    valid = users[users['mail'].str.match(pattern, na=False)]
    return valid