# 2차원 데이터 구조
# excel 문서의 시트와 유사
# 행과 열로 구성
# 각 열별로 데이터 타입을 가짐
# 시리즈 + 칼럼

import pandas as pd
import numpy as np

# list 를 통한 생성
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
df = pd.DataFrame([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(df)


# np 를 통한 생성
df = pd.DataFrame(np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
]))

print(df)

# dictionary 를 통한 생성 방법
data = {
    '이름': ['김철수', '이영희', '홍길동'],
    '학교': ['서울고', '대전고', '경기고'],
    '점수': [80, 95, 85]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame([
    [1,2,3],
    [4,5,6],
    [7,8,9]
], columns=['가','나','다'], index=['a', 'b', 'c'])

print(df)

# 속성 확인
print(df.index)
# Index(['a', 'b', 'c'], dtype='object')

print(df.columns)
# Index(['가', '나', '다'], dtype='object')

# 데이터 값을 추출하시오. 
print(df.values)
print(type(df.values))
print(type(df.dtypes))

print(df)
print(df.dtypes)

# 가    int64
# 나    int64
# 다    int64

# 인덱스 지정

df.index = ['1번', '2번', '3번']
print(df)

df = pd.DataFrame(
    {'이름': ['김철수', '이영희', '박철수'],
     '학교': ['서울고', '대전고', '경기고'],
     '점수': [80, 95, 85]
    }
)
# 컬럼 다루기

# 1번 김철수
# 2번 이영희
# 3번 홍길동

# 두 개 이상 컬럼 가지고 오기
print(df[['이름', '점수']])

print(df['이름'])
print(df[['이름']]) # 시리즈로 갖고 옴

# 컬럼 이름 변경
df = df.rename(columns={'이름': 'name', '점수': 'score'})
print(df)

