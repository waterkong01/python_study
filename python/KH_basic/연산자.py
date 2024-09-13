# 프로그램에서 값을 연산해야 하는 경우 사용
# 산술연산자 : +, -, *, /, //, %, **
i = 10
j = 3
print(i + j) # 더하기
print(i - j) # 빼기
print(i * j) # 곱하기
print(i / j) # 나누기
print(i // j) # 몫
print(i % j) # 나머지, 알고리즘 문제에서 많이 사용
print(i ** j) # 제곱근

TAX_RATE = 0.10 # 세율
income = int(input("당신의 수입은 얼마 입니까?"))
print(f"당신이 내야 할 세금은 {income * TAX_RATE}")

# 대입 연산자 : 값을 변수에 대입 (=)
# 대입 연산자 종류 : =, +=, -=, *=, /=, %= (=을 제외하고는 복합 대입 연산자)
num1 = 10
num1 += 2 # num1 = num1 + 2
print(num1) # 결과는 12
num1 -=10 # num1 = num1 - 10
print(num1) # 결과는 2

num1 *= 2
print(num1) # 결과는 4

# 비교 연산자 : 두 개의 값을 비교해서 참/거짓
# == 같다, > 왼쪽이 크다, >= 왼쪽이 크거나 같다, < 오른쪽이 크다, <= 오른쪽이 크거나 같다, != 같지 않다
a = 10
b = 20
print(a > b) # False
print(a < b) # True
print(a == b) # False
print(a >= b) # False
print(a <= b) # True
print(a != b) # True

# 관계 연산자 : and(&&) 둘 다 참이면 참, or(||) 둘 중 하나만 참이면 참, not(!) 참이면 거짓/거짓이면 참
x = 10
y = 20
z = 30
rst1 = (x > 0) and (x > y) # rst1 = True and False = False
rst2 = (x > 0) or (x > y) # rst2 = True or False = True
rst3 = not((x > 0) or (x > y)) # rst3 = not(True or False) = not(True) = False

# 3항 연산자 : 항이 3개인 연산자 : 참과 거짓이 있는 조건문과 동일
age = int(input("나이를 입력하세요 : "))
# is_adult = age > 19 and "성인" or "미성년자"
# print(f"당신은 {is_adult} 입니다.")

# if age > 19:
#     print(f"당신은 성인입니다.")
# else:
#     print(f"당신은 미성년자입니다.")

