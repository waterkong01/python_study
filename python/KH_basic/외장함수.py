# 외장함수 : import 해서 사용하는 함수, 파이썬이 기본적으로 제공하는 것 (별도의 모듈 설치X)

# 랜덤 함수 : 지정한 범위 내에서 임의의 숫자를 만들어 내는 것
# import  random
# for i in range(10):
#     rand = random.randint(0, 4) # 0~4 까지의 임의의 값을 생성
#     # rand = random.randrange(0, 10) # 0~10 미만
#     print(rand, end=" ")
# print()

# 중복되지 않는 로또 번호 생성 : 1~45 사이의 임의의 수 6개
# 리스트를 사용하고, 리스트내에 임의로 생성한 번호가 있으면 추가X)
import random

print("로또 번호 자동 생성 : ", end=" ")

# ver1
lotto = []
while True:
    rand = random.randint(1, 45)
    if rand not in lotto:
        lotto.append(rand)
    if len(lotto) == 6:
        break
print(lotto)

# ver2
lotto = []
while len(lotto) <= 6:
    rand = random.randrange(1, 46)
    if rand not in lotto:
        lotto.append(rand)
print(lotto)

# ver3 중복을 제거하는 특징을 가진 집합(set)을 사용했기 때문에 중복X
lotto = set()
while len(lotto) <= 6:
    rand = random.randrange(1, 46)
    lotto.add(rand)
print(lotto)