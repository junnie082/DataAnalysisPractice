import numpy as np

arr = np.array([
                [1, 2, 3],
                [0, 1, 4]
              ])

# 배열 전체
print(np.min(arr))
print(arr.min())

# 최솟값
print(arr.min(axis=0))
# [0 1 3]
print(arr.min(axis=1))
# [1 0]

# 최댓값
print(np.max(arr))
print(arr.max())
print(arr.max(axis=0))
# [1 2 4]
print(arr.max(axis=1))
# [3 4]

# 원소 합/ 누적합
print(np.sum(arr))
print(arr.sum())

print(arr.sum(axis=0)) # 각 열에 대한 모든 행에서 동작
print(arr.sum(axis=1)) # 각 행에 대한 모든 열에서 동작


# 누적 합계
# "cumulative sum", 즉 누적 합계
# 앞에서부터 차례로 더한 값을 반환
print(np.cumsum(arr)) # 1차원 배열로 생성
print(arr.cumsum()) # 1차원 배열로 생성

print(arr.cumsum(axis=0)) # 각 열에 대한 모든 행에서 동작
print(arr.cumsum(axis=1)) # 각 행에 대한 모든 열에서 동작


# arr = np.array([
#                 [1, 2, 3],
#                 [0, 1, 4]
#               ])

# 평균/표준편차/중앙값/
#평균
print(np.mean(arr))
print(arr.mean())
print(arr.mean(axis=0)) # 각 열에 대한 모든 행에서 동작
print(arr.mean(axis=1)) # 각 행에 대한 모든 열에서 동작

# 표준편차
print(np.std(arr))
print(arr.std())
print(arr.std(axis=0)) # 각 열에 대한 모든 행에서 동작
print(arr.std(axis=1)) # 각 행에 대한 모든 열에서 동작

# 중앙값

# 중앙값은 정렬된 배열의 가운데 값입니다. 
# 원소 개수가 **짝수(6개)** 이므로
# 가운데 두 값의 평균 -> (1+2)/2 = 1.5

print(np.median(arr))
# print(arr.median())
# print(arr.median(axis=0)) # 각 열에 대한 모든 행에서 동작
# print(arr.median(axis=1)) # 각 행에 대한 모든 열에서 동작

# 비교연산
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
                 
arr2 = np.array([[1, 0, 3],
                 [4, -2, 9]])
                 
print(arr1 == arr2)
print(arr1 > arr2)

# 배열 전체의 동일 여부 (배열 전체의 값을 비교)
print(np.array_equal(arr1, arr2))
