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

# 컬럼 내용 수정하기
df['지역'].replace({'서울': '경기', '부산': '대구'}, inplace=True)
print(df)

# 대소문자가 섞여 있는 '코딩' 칼럼을 모두 소문자로 바꾸고 싶음
# def to_lower(word): 
#     return str(word).lower()

# df['코딩'] = df['코딩'].apply(to_lower)
# print(df)

df['코딩'] = df['코딩'].str.lower()
print(df)

# 대소문자가 섞여 있는 '코딩' 칼럼을 모두 대문자로 바꾸고 싶음
df['코딩'] = df['코딩'].str.upper()
print(df)

## 기억하기
## .str 
# 해당 열이 문자열(sring)일 경우, 문자열 관련 메서드를 적용할 수 있게 해줌

# 컬럼 추가
# 없으면 추가, 있으면 해당 값 업데이트
df['점수총합'] = df['국어점수'] + df['수학점수']
print(df)

# 점수 총합에 10점씩 더하기
# df['점수총합'] = df['점수총합'] + 10
# print(df)

# 결과 컬럼 생성 후, '불합격'으로 초기화하기
df['결과'] = '불합격'
print(df)

# 총합 160 넘으면 '합격'
# condition = df['점수총합'] > 160

# df['결과'] = ['합격' if condition else '불합격']
# print(df)

# df.loc[ 행, 렬 ]
df.loc[df['점수총합'] > 160, "결과"] = "합격"
print(df)

# 컬럼 삭제
df.drop(columns=['점수총합'], inplace=True)
print(df)

# 행단위 CRUD
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

# 행추가
df.loc["7번"] = ["길", "부산", 22, 90, 90, "kotlin"]
print(df)

# 셀수정
df.loc["4번", "국어점수"] = 100
print(df) 

# 두개 이상의 행의 값을 변경 할 때
df.loc["4번", ["지역", "코딩"]] = ["대구", "C"]
print(df)

df.loc["1번", ["지역", "나이"]] = ["경기", 20]
print(df)

# 7번 삭제
df = df.drop("7번")
print(df)

df = df[df['이름'] != '길']
print(df)