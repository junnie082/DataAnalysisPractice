import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# 30 보다 큰 값만 선택
# 첫 번째 방법
for value in arr: 
    if value > 30: 
        print(value)
        
# 루비가 생각한 두 번째 방법
func = lambda x: x > 30
result = func(arr)
print(result)
        
# 그런데 넘파이 배열에서는 for 문을 돌리면 왕따 당함
# for 문 안돌리려고 numpy 배열 쓰는 거임ㅋㅋ

condition = arr > 30 # __gt__ 함수로 구현해 놓아서 함수 오버라이딩 해놓았기 때문에 가능한 거임. 
# __gt__ 는 내부적으로 for 문을 돌리고 있음. 
print(condition)
result = arr[condition]
print(result)

print(arr[arr>30])
# __gt__
# arr 는 객체 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 조건: 짝수만 선택
print(arr[arr % 2 == 0])

# 1부터 100까지의 배열을 만들고 그중에서 7의 배수이자 11의 배수인 숫자만 뽑아ㄴ시오
arr = np.arange(1, 1001)
subarr = arr[arr % 7 == 0]
result = subarr[subarr % 11 == 0]
print(result)


arr = np.arange(1, 1001)
# print(arr[arr % 7 == 0 and arr % 11 ==0]) -> 이건 안됨
# print(arr[arr[arr % 7 == 0] % 11 == 0]) -> 이것도 오답

# 강사의 답: 
arr = np.arange(1, 1001)
# result = arr[(arr % 7 == 0) and (arr % 11 == 0)]
# -> and 가 if 문에서는 먹히는데 이 경우에는 and 가 먹히지 않는다. 즉,
result = arr[(arr % 7 == 0) & (arr % 11 == 0)]

# Numpy 배열 연산에서는 | & (파이프 기호)
# 파이썬 기본 문법은 and or
print(result)

# 1부터 1000까지의 배열 짝수이거나 100의 배수
print(arr[(arr % 2 == 0) | (arr % 100 == 0)])

