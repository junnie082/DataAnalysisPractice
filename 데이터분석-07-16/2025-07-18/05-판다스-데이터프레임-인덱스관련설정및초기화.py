import pandas as pd
import numpy as np

data = {
    '이름': ['김철수', '이영희', '홍길동'], 
    '학교': ['서울고', '대전고', '경기고'], 
    '점수': [80, 95, 85]
}

df = pd.DataFrame(data)
print(df)

# 인덱스 수정
df.index = ['1번', '2번', '3번']
print(df)

# 인덱스 이름 설정
df.index.name = '번호'
print(df)

# 번호
# 1번  김철수  서울고  80
# 2번  이영희  대전고  95
# 3번  홍길동  경기고  85

# 인덱스 초기화
df.reset_index(inplace=True)
print(df)

# 아까 전에는 '번호'가 index 였는데 reset_index 를 하게 되면 '번호'가 컬럼으로 들어가게 됨.

# 인덱스 설정
df.set_index('이름', inplace=True)
print(df)

# 인덱스 정렬
df.sort_index(ascending=False, inplace=True)
print(df)

# 수학점수가 높은 순으로 정렬하고, 동일한 점수일 경우 이름을 기준으로 오름차순 정렬하라. 
print(df.sort_values(['수학점수', '이름'], ascending=[True, False]))