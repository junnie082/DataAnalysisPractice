import numpy as np

arr = np.array([0, 1, 2, 3, 4])

# 넘파이 배열을 읽는 방법은 리스트의 인덱싱과 같음
print(arr[2])
print(arr[-1])
print(arr[-2])

arr[0] = 2
print(arr)

# print(arr.dtype)
# arr[0] = "없음" -> 이건 안됨. 
# print(arr)

arr = np.array([
    [0, 1, 2],
    [3, 4, 5]
])


# 문제
# 1) 해당  배열의 차원을 출력하시오
# 2) 0을 뽑아 내시오
# 3) 5을 뽑아 내시오
print(arr.shape)
print(arr[0, 0])
print(arr[1, 2])
print(arr[-1, -1])

# arr[0, 0] 과 arr[0][0] 는 데이터 접근 방법만 다를 뿐, 결과는 같음
# arr[0][0] 같은 경우는 [0, 1, 2][0] 과 같음

# 슬라이싱
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print("원본 배열:", arr)

# 문제 
# 인덱스 1부터 3까지
print(arr[1:4])

# 인덱스 4부터 끝까지
print(arr[4:])

# 처음부터 끝까지, 2칸씩 건너뛰기
print(arr[::2])

# 마지막 3개 원소
print(arr[-3:])

# 2차원 배열 슬라이싱
arr = np.array([
    [0,1,2,3],
    [4,5,6,7]
])
print(arr.shape)

# 첫번째 행 전체
print(arr[0])
print(arr[0,:])

# 두번째 행 전체
print(arr[1,:])

# 두번째 열 전체
print(arr[:,1])

# 두번째 행의 두번째 열부터 끝열까지
print(arr[1, 1:])

