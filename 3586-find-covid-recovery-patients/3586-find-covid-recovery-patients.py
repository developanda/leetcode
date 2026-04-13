import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
 # ──────────────────────────────────────────────
    # Step 1. 날짜 컬럼 타입 변환
    #   - test_date가 문자열로 들어올 수 있으므로
    #     날짜 연산이 가능하도록 datetime 형식으로 변환
    # ──────────────────────────────────────────────
    covid_tests["test_date"] = pd.to_datetime(covid_tests["test_date"])
 
 
    # ──────────────────────────────────────────────
    # Step 2. 각 환자의 '첫 번째 양성(Positive) 검사일' 추출
    #   - 양성 기록만 필터링한 뒤
    #   - 환자별로 가장 빠른(min) 날짜를 구함
    # ──────────────────────────────────────────────
    first_positive = (
        covid_tests[covid_tests["result"] == "Positive"]   # 양성 행만 선택
        .groupby("patient_id", as_index=False)["test_date"] # 환자별 그룹
        .min()                                               # 가장 이른 날짜
        .rename(columns={"test_date": "first_positive_date"})
    )
 
 
    # ──────────────────────────────────────────────
    # Step 3. 첫 양성일 이후의 '첫 번째 음성(Negative) 검사일' 추출
    #   - 음성 기록을 가져와서, 첫 양성일 정보와 join
    #   - 음성 검사일이 첫 양성일보다 '이후' 인 행만 유지
    #   - 이후 환자별 가장 빠른 음성일 선택
    # ──────────────────────────────────────────────
    # 3-a. 음성 검사 기록 전체를 첫 양성일 테이블과 결합
    negative_tests = (
        covid_tests[covid_tests["result"] == "Negative"]    # 음성 행만 선택
        .merge(first_positive, on="patient_id")             # 첫 양성일 정보 붙이기
    )
 
    # 3-b. 음성 검사일이 첫 양성일보다 이후인 행만 필터
    #   → 양성 판정 이전의 음성 기록은 '회복'으로 인정하지 않음
    valid_negative = negative_tests[
        negative_tests["test_date"] > negative_tests["first_positive_date"]
    ]
 
    # 3-c. 조건을 충족하는 음성 검사 중 가장 이른 날짜 선택
    first_negative_after_positive = (
        valid_negative
        .groupby("patient_id", as_index=False)["test_date"]
        .min()
        .rename(columns={"test_date": "first_negative_date"})
    )
 
 
    # ──────────────────────────────────────────────
    # Step 4. 회복 기간(recovery_time) 계산
    #   - 첫 양성일 테이블과 첫 음성일 테이블을 결합
    #   - 두 날짜의 차이(일수)를 recovery_time으로 저장
    #   - inner join → 양쪽 모두 존재하는 환자만 결과에 포함됨
    #     (양성만 있거나, 음성만 있는 환자는 자동으로 제외)
    # ──────────────────────────────────────────────
    recovery_df = first_positive.merge(
        first_negative_after_positive,
        on="patient_id"
    )
 
    recovery_df["recovery_time"] = (
        recovery_df["first_negative_date"] - recovery_df["first_positive_date"]
    ).dt.days  # timedelta → 정수(일수) 변환
 
 
    # ──────────────────────────────────────────────
    # Step 5. 환자 기본 정보(patients 테이블)와 결합
    #   - patient_name, age 컬럼을 붙이기 위해 join
    # ──────────────────────────────────────────────
    result = recovery_df.merge(patients, on="patient_id")
 
 
    # ──────────────────────────────────────────────
    # Step 6. 출력 컬럼 선택 및 정렬
    #   - 요구 컬럼: patient_id, patient_name, age, recovery_time
    #   - 정렬 기준: recovery_time 오름차순 → patient_name 오름차순
    # ──────────────────────────────────────────────
    result = (
        result[["patient_id", "patient_name", "age", "recovery_time"]]
        .sort_values(by=["recovery_time", "patient_name"])
        .reset_index(drop=True)  # 인덱스 재정렬 (보기 좋게)
    )
 
    return result