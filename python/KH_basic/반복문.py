# # 조건이 참인 동안 반복 수행
# n = int(input("정수 입력 : "))
# sum = 0 # 값을 누적 하기 위한 함수
# 
# while n: # 0이 아닌 모든 값은 참으로 간주 (java 제외 java에서는 조건식을 넣어야 함)
#     sum += n
#     n -= 1 # n = n - 1, n--
#     print(sum) # while문 안에 있으면 계산 할 때마다 결과 출력
# 
# 
# for i in range(1, n + 1): # 범위 기반
#     sum += i
# print(sum)
# 
# # while문은 주로 횟수가 정해지지 않은 반복적인 수행
# while True: # 반복문 내에 탈출 조건이 있어야 함(break)
#     age = int(input("나이를 입력하세요 : "))
#     if 0 < age <150:
#         break
#     else:
#         print("나이를 다시 입력해주세요.")
#         
# # for문 : 정해진 범위 만큼을 반복 수행할 때 효과적
# # for 요소 in 시퀀스: (시퀀스 자료에 대한 자동 순회, 요소에 i 대신 e 사용(i는 인덱스로 착각 가능))
# fruits = ["apple", "banana", "lemon"]
# for fruit in fruits:
#     print(fruit)
# 
# name = "abcdefg"
# for e in name:
#     print(e, end="-")
# 
# for e in input("문자열 입력 : "):
#     print(e, end="-")
# 
# # for 인덱스 in range(시작값, 종료값, 증감값):
# n = int(input("정수 입력 : "))
# sum = 0
# for i in range(1, n + 1, 2): # 시작값이 0인 경우, 증감값이 1인 경우 생략 가능
#     sum += i
# print(sum)
# 
# # 이중 for문 사용하기
# n = int(input("정수 입력 : "))
# for i  in range(n): # 0에서 n미만까지
#     print(f"i = {i}", end="")
#     for j in range(n):
#         print("*", end=" ")
#     print()
# 
#
# # 이중 for문 구구단 구하기
# for i in range(2, 10): # 2단에서 9단
#     for j in range(1, 10): # 1~9 곱하기
#         print(f"{i} X {j} = {i * j}")
#     print("-" * 20) # 경계선("-" 20개로 각 단 분리)
#
# # 제어문 : break, continue
# # break : 반복문을 탈출할 때 사용
# # continue : 아래의 문장을 수행하지 않고 반복문의 조건식으로 이동 (해당 루틴을 수행한 것으로 간주)
#
# n = int(input("정수 입력 : "))
# for i in range(n):
#     if i % 2 == 0: # 짝수이면 아래의 문장(print(i))을 수행하지 않음
#         continue
#     print(i)
#
# # 반복문 역순
# n = int(input("정수 입력 : "))
# for i in range(n, 0 - 1, -1): # n ~ 0, 1씩 차감
#     print(f"인덱스 : {i}")
#
# for문으로 알파벳 출력
# ASCII
# chr() : 유니코드를 입력 받아 그 코드에 해당하는 문자 출력
# ord() : 문자의 유니코드 값을 돌려주는 함수

for i in range(ord("A"), ord("Z") + 1):
    print(chr(i), end=" ")
print()

for i in range(65, 91):
    print(chr(i), end=" ")
print()