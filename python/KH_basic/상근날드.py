# 햄버거 가격 3개
# 음료 가격 2개
# 출력 : 세트 메뉴 가격 = (햄버거 3개 중 가장 싼 것 + 음료 2개 중 싼 것 - 50)원
# 입력 : 1000 1500 3000 1200 750
# 세트 : 1700원

price = list(map(int, input("햄버거 3개, 음료 2개 가격 입력 : ").split()))

# ver1
min_burger = min(price[:3])
min_drink = min(price[3:5])
print(f"세트 가격 : {min_burger + min_drink - 50}원")


# ver2
min_burger = price[0] # 기준값 정하기
min_drink = price[3]

for i in range(len(price)):
    if i < 3 and min_burger > price[i]:
        min_burger = price[i]
    if i > 2 and min_drink > price[i]:
        min_drink = price[i]
print(f"세트 가격 : {min_burger + min_drink - 50}원")