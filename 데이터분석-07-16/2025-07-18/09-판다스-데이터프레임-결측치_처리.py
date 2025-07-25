import pandas as pd
import numpy as np

# 결측치란 데이터에서 누락된 값 또는 빠진 값을 말합니다. 
# 결측치가 문제가 되는 이유
# 통계 분석이나 머신러닝 모델에서 왜곡된 결과를 초래할 수 있음

data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', np.nan, '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', np.nan, 'Javascript', 'PYTHON', np.nan]
}

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
print(df)

# 데이터프레임의 '지역' 컬럼 내 데이터들을 모두 결측치로 지정
# df['지역'] = np.nan
# print(df)

# df.fillna('없음', inplace=True)
# print(df)

# 특정 열을 지정하여 처리하기 
# df['코딩'].fillna('없음', inplace=True)
# print(df)

# 데이터 삭제

#      이름   지역  나이  국어점수  수학점수          코딩
# 1번  유재석   서울  19    86    86      Python
# 2번  박명수   부산  23    90   100        Java
# 3번  정준하  NaN  20    80    66          없음
# 4번  노홍철   서울  25    65    70  Javascript
# 4번  노홍철   서울  25    65    70  Javascript
# 5번  정형돈   서울  18    50    40      PYTHON
# 6번   하하   서울  21    60    80          없음

# NaN 을 가진 모든 행 삭제
# df.dropna(inplace=True)
# 이름  지역  나이  국어점수  수학점수          코딩
# 1번  유재석  서울  19    86    86      Python
# 2번  박명수  부산  23    90   100        Java
# 4번  노홍철  서울  25    65    70  Javascript
# 5번  정형돈  서울  18    50    40      PYTHON
# 6번   하하  서울  21    60    80          없음
print(df)
# df.dropna(axis='index', how='any', inplace=True) # NaN이 하나라도 있는 row 삭제
# print(df)
df.dropna(axis='columns', how='any', inplace=True) # NaN이 하나라도 있는 col 삭제
# 모든 게 NaN 일때는 how 에 'all' 을 넣어주어야 함
print(df)

# 이름   지역  나이  국어점수  수학점수          코딩
# 1번  유재석   서울  19    86    86      Python
# 2번  박명수   부산  23    90   100        Java
# 3번  정준하  NaN  20    80    66         NaN
# 4번  노홍철   서울  25    65    70  Javascript
# 5번  정형돈   서울  18    50    40      PYTHON
# 6번   하하   서울  21    60    80         NaN

