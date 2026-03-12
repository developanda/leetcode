import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    result = user_content.copy()
    # 컬럼명 변경 (기존 content_text가 있을 것으로 가정)
    result.columns = ['content_id', 'original_text']
    
    def transform_text(text):
        if pd.isna(text): return text
        
        # 1. 공백 기준 capitalize (첫 단어 대문자)
        words = [word.capitalize() for word in str(text).split(' ')]
        intermediate = ' '.join(words)
        
        # 2. 하이픈(-) 조건 처리
        # "--"가 있거나 " -"가 있는 경우 그대로 반환 (사용자 로직 반영)
        if "--" in intermediate or " -" in intermediate:
            return intermediate
        else:
            # 하이픈으로 연결된 각 단어의 첫 글자를 대문자로
            return '-'.join([w[0].upper() + w[1:] if len(w) > 0 else w 
                             for w in intermediate.split('-')])

    # apply를 사용하여 한 번에 처리
    result['converted_text'] = result['original_text'].apply(transform_text)
    
    return result