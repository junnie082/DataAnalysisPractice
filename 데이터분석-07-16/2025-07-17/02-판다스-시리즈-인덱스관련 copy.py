# 인덱스 관련
 
import pandas as pd
import numpy as np

# 딕셔너리 생성시 자동으로 키가 시리즈의 인덱스로 들어감
series = pd.Series({'사과': 1200, '딸기': 3500, '키위': 2100, '메론': 9600})
print(series)

series = pd.Series([1200, 3500, 2100, 9600], index=['사과', '딸기', '키위', '메론'])
print(series)

# 시리즈 속성확인
print(series.index)
print(series.values)
print(series.ndim)
print(series.shape)

series.name = '과일가격'
print(series)

#   사과    1200
#   딸기    3500
#   키위    2100
#   메론    9600
#   Name: 과일가격, dtype: int64

# 인덱스 수정
# 인덱스 수정은 전체 수정 가능, 일부 수정 불가
series.index = ['오렌지', '딸기', '키위', '메론']
print(series)

#   series.index[0] = '키위'


