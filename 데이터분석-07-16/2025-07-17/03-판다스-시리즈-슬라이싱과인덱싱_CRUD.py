import pandas as pd

# 딕셔너리로 생성시 자동으로 키가 시리즈의 인덱스로 들어감
series =  pd.Series([1200, 3500, 2100, 9600],
              index=['사과', '딸기', '키위', '메론'])
print(series)

# 단일값 접근
print(series['사과']) # 1200
print(series[['사과']]) # -> 리스트로 묶어야 시리즈로 반환됨 
# 사과    1200
# dtype: int64

# 여러값 접근
print(series[['사과', '딸기', '키위']])

# 과일 중에 2100 초과한 과일을 시리즈로 뽑아내시오
# 조건 필터링을 통한 접근(불린 인덱싱)
print(series[series > 2100])

# 행번호 기반 슬라이싱
print(series[1:3]) 
print(series[0])
print(series[:])

# 라벨기반 인덱싱
print(series['사과':'메론'])
print(series['사과': '딸기'])
print(series[['사과', '메론']])

# loc(라벨기반 함수)와 iloc(행번호) 기반 인덱싱
print(series.loc['사과':'딸기'])
print(series.iloc[1:3])
# 특정 위치의 값 접근
print(series.iloc[0])
print(series.iloc[-1])

# 시리즈 추가
series.loc["바나나"] = 5000
print(series)

series.loc["바나나"] = 7000
print(series)

series.iloc[-1] = 8000
print(series)

# 삭제 
# series.drop("사과", inplace=True) 
series = series.drop("사과")
print(series)

series.drop(['딸기', '바나나'], inplace=True)
print(series)

