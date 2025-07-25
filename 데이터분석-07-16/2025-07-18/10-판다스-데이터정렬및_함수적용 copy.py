import pandas as pd
import numpy as np

# 결측치란 데이터에서 누락된 값 또는 빠진 값을 말합니다. 
# 결측치가 문제가 되는 이유
# 통계 분석이나 머신러닝 모델에서 왜곡된 결과를 초래할 수 있음

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

# 정렬
print(df.sort_index())
print(df.sort_index(ascending=True))
print(df.sort_index(ascending=False))

# 컬럼 기준
print(df.sort_values('나이', ascending=True))
print(df.sort_values('나이', ascending=False))

# 이름 순으로 정렬하시오
print(df.sort_values('이름', ascending=True))

# 두개를 기준으로 적용하기

# 이름   지역  나이  국어점수  수학점수          코딩
# 2번  박명수   부산  23    90   100        Java
# 5번  정형돈   서울  18    50    40      PYTHON
# 1번  유재석   서울  19    86    86      Python
# 6번   하하   서울  21    60    80         NaN
# 4번  노홍철   서울  25    65    70  Javascript
# 3번  정준하  NaN  20    80    66         NaN
print(df.sort_values(['지역', '나이']))

print(df.sort_values(['지역', '나이'], ascending=[True,False]))

# 수학점수가 높은 순으로 정렬하고, 동일한 점수일 경우 이름을 기준으로 오름차순 정렬하라
print(df.sort_values(['수학점수', '이름'], ascending=[False, True]))

# 특정 컬럼을 시리즈로 불러와 정렬
print(df['수학점수'].sort_values())

# 함수 적용 - apply 
# 데이터 전처리 과정에서 특정 열이나 행을 변환해야 할 때가 있음
# apply() 함수를 데이터 적용

def add_s(age): 
    return str(age) + '세'

df['나이'] = df['나이'].apply(add_s)
print(df)

# 나이에서 '세' 제거하고 정수형으로 변환
df['나이'] = df['나이'].str.replace('세', '').astype(int)
print(df)

# apply() 함수를 적용하여 
# 국어 점수 5점 올리기
def add_five(score): 
    return score + 5

print(df['국어점수'].apply(add_five))

# 아니면
df['국어점수'] = df['국어점수'] + 5 # 데이터 타입이 모두 동일하므로 
print(df)

# 코딩에 들어가는 문자를 모두 대문자로 하시오. 
def lower_to_upper(word): 
    return str(word).upper()

# df.dropna(axis='index', how='any', inplace=True) # NaN이 하나라도 있는 col 삭제
# df = df.apply(lower_to_upper)
# print(df)
print(df['코딩'].apply(lower_to_upper))

# 국어점수와 수학점수의 평균을 구하고, 평균 컬럼으로 저장하시오. 
def test_avg(row): 
    return (row['수학점수'] + row['국어점수']) / 2

df['평균'] = df.apply(test_avg, axis=1) # 행으로 넘기기 위해서 axis=1 이 필요함. 
print(df)

# 90점 이상 A 
# 80점 이상 B 
# 70점 이상 C
# 나머지 F 
def grade(score):
    if score >= 90: 
        return 'A'
    elif score >= 80: 
        return'B'
    elif score >= 70: 
        return 'C'
    else:
        return 'F' 
    
df['등급'] = df['평균'].apply(grade)
print(df)

