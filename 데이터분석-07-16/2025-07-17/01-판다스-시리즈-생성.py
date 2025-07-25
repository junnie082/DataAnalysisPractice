# 차원 배열 구조 - Series: 1차원 배열
# 인덱스(index) 사용 가능 - 인덱싱/슬라이싱
# 데이터 타입을 가짐 (dtype)

import pandas as pd
import numpy as np

# numpy 배열로 시리즈 생성
arr = np.arange(100, 105)
print(arr)


#    0    100
#    1    101
#    2    102
#    3    103
#    4    104
series = pd.Series(arr)
print(type(series))
print(series)

series = pd.Series(arr, dtype='int32')
print(type(series))
print(series)

# list로 생성
series = pd.Series([100, 200, 300, 400])
print(type(series))
print(series)

series = pd.Series(['사과', '딸기', '포도', '수박', '참외'])
print(type(series))
print(series)

series = pd.Series([91, 3.14, '포도', 4, 77])
print(type(series))
print(series)

# 딕셔너리

# a    100
# b    200
# c    300
# dtype: int64
data ={'a': 100, 'b': 200, 'c': 300}
series = pd.Series(data)
print(series)

