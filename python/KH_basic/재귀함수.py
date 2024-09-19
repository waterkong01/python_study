# 재귀함수 - 함수 내에서 자기 자신을 호출하는 구조
# 알고리즘(길찾기, 효율적인 정렬 등) 구현 시 많이 사용

# [1]
def for_sum(n):
    s = 0
    for i in range(1, n + 1):       # 1부터 n까지의 합
        s += i
    return s
num = int(input("정수 입력 : "))
print(for_sum(num))

# [2]
def while_sum(n):
    s = 0
    while True:
        s += n
        n -= 1
        if n == 0:
            break
    return s
num = int(input("정수 입력 : "))
print(while_sum(num))

# [3]
def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)
num = int(input("정수 입력 : "))
print(recursive_sum(num))