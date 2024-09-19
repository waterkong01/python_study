# 입력 받은 수 미만의 소수의 합 구하기
# 입력 : 12
# 2, 3, 5, 7, 11
# 출력: 28
from mypy.checker import is_private

def prime_func(n):
    is_prime = True
    for i in range(2, n):       # 1과 자기 자신 제외 (2~(입력받은 수))
        if n % i == 0:      # n을 i로 나눴을 때 나머지가 0이면
            is_prime = False        # is_prime = False
    if is_prime:
        return n        # 소수가 맞으면 n 반환
    else:
        return 0        # 소수가 아니면 0 반환

n = int(input("정수 입력 : "))
# is_prime = prime_func(n)
# if is_prime:
#     print("소수 입니다.")
# else:
#     print("소수가 아닙니다.")
sum = 0     # sum을 0으로 초기화
for i in range(2, n):       # 1과 자기 자신 제외
    sum += prime_func(i)        # sum에 prime_func(i) 값 누적 합
print(sum)      # 누적된 sum 출력