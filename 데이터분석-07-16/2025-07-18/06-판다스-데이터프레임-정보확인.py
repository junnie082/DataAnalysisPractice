import pandas as pd
import numpy as np
data = {
    '이름' : ['유재석', '박명수', '정준하', '노홍철', '정형돈', '하하'],
    '지역' : ['서울', '부산', '부산', '서울', '서울', '서울'],
    '나이' : [19, 23, 20, 25, 18, 21],
    '국어점수' : [86, 90, 80, 65, 50, 60],
    '수학점수' : [86, 100, 66, 70, 40, 80],
    '코딩' : ['Python', 'Java', np.nan, 'Javascript', 'PYTHON', np.nan]
}
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
print(df)

df.info() # print(df.info()) 는 하지 말 것. df.info() 안에 이미 print() 가 있음.
#      이름  지역  나이  국어점수  수학점수          코딩
# 1번  유재석  서울  19    86    86      Python
# 2번  박명수  부산  23    90   100        Java
# 3번  정준하  부산  20    80    66         NaN
# 4번  노홍철  서울  25    65    70  Javascript
# 5번  정형돈  서울  18    50    40      PYTHON
# 6번   하하  서울  21    60    80         NaN
print(df.describe())
#               나이       국어점수        수학점수
# count   6.000000   6.000000    6.000000
# mean   21.000000  71.833333   73.666667
# std     2.607681  15.879757   20.451569
# min    18.000000  50.000000   40.000000
# 25%    19.250000  61.250000   67.000000
# 50%    20.500000  72.500000   75.000000
# 75%    22.500000  84.500000   84.500000
# max    25.000000  90.000000  100.000000

print(df.head()) # 디폴트는 위에서 다섯 개. 
print(df.head(10))
print(df.tail()) # 디폴트는 밑에서 다섯 개. 
print(df.shape) # 요즘 잘 안씀

# 데이터 프레임에서 시리즈 처리
print(df['국어점수'].describe())
print('-----')
print('min')
print(df['국어점수'].min())
print('max')
print(df['국어점수'].max)
print('----')
print(df['국어점수'].mean())
print(df['국어점수'].sum())

print(df['국어점수'].count())

# 컬럼 코딩에 들어 있는 데이터 캣수
print(df['코딩'].count()) # Nan 은 카운트가 안됨. 
