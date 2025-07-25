# 정렬
import numpy as np

arr = np.random.randint(10, size =10)
print(arr)
print(np.sort(arr)) # 원본에 영향을 주지 못함
print(arr)
arr.sort()
print(arr)

# 내림차순
print(np.sort(arr)[::-1]) 

arr.sort()
# arr = np.sort(arr)[::-1]# 원래 배열까지 바꿀 수 있음
print(arr[::-1])

np.random.seed(42)  # 시드 값 고정
# 2차원 배열
arr = np.random.randint(15, size=(3,4))


# [[ 6  3 12 14]
#  [10  7 12  4]
#  [ 6  9  2  6]]
print(arr)

print(np.sort(arr))

# [[ 6  3  2  4]
#  [ 6  7 12  6]
#  [10  9 12 14]]
print(np.sort(arr, axis=0)) # 열단위 (axis = 0 가장 바깥쪽에 있는 괄호)

# [ 3  6 12 14]
# [ 4  7 10 12]
#[ 2  6  6  9]]
print(np.sort(arr, axis=1)) # 행단위 (axis = 1 그 다음 안쪽에 있는 괄호)

# 디폴트 값은 axis = 1 이므로 해당 어트리뷰트를 설정하지 않으면 axis = 1 로 설정이 자동으로 됨. 