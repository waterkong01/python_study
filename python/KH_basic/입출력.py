# 표준 입출력 : 콘솔 입출력을 의미
# [] 대괄호 : 리스트를 표시
# {} 중괄호 : 딕셔너리 표시
# () 소괄호 : 함수의 인수, 튜플 표시
from time import sleep

from debugpy.launcher.debuggee import job_handle
from numpy.core.numerictypes import generic
from pyasn1_modules.rfc2985 import gender
from zope.interface import named

# print() : 화면 출력을 위한 함수
print(35)
print("문자열")
print([1, 2, 3, 4, 5]) # 리스트  출력
print("파"+"이"+"썬") # '+'는 문자열을 이어주는 연산자
print("파", "이", "썬", sep = " ") # ',(콤마)'는 구분자를 의미, 구분자의 기본값은 공백
print("파""이""썬")

# 이스케이프 문자 : 출력 구간의 흐름을 제어
# \n(줄바꿈), \t(tab(탭), \b(백스페이스), \r(커서를 맨 앞으로 이동)

print("\n\n", sep = " ", end = "\n")
print("Banana\b")
print("Banana\rApple")

# import time
# for i in range(1, 101):
#     time.sleep(1)
#     print(f"\r{i}%", end="")

# 출력 스타일 정리
name = "하수빈"
age = 24
gender = "여성"
job = "개발자"
addr = "서울시 강북구"

# 서식지정자 스타일 (C언어 방법)
print("========== 서식 지정자 스타일 ==========")
print("이름 : %s / 성별 : %s"%(name, gender))
print("나이 : %d"%age)
print("주소: %s"%addr)

# 파이썬 old 스타일
print("========== 파이썬 OLD 스타일 ==========")
print("이름 : {} / 성별 : {}".format(name, gender))
print("주소 : {}".format(addr))

# 파이썬 현재 스타일
print("========== 파이썬 현재 스타일 ==========")
print(f"이름 : {name} / 성별 : {gender}")
print(f"주소 : {addr}")

# 문자열 연결 연산자 사용 방식
print("이름 : " + name)
print("나이 : " + str(age))

# 정렬
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.14592945844509804586045968

print(f"|{num1:^8}|")
print(f"|{num2:^8}|")
print(f"|{num3:^8}|")
print(f"|{num4:^8}|")
print(f"{num5:.3f}|")
