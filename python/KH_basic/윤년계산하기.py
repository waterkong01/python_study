# 연도가 4로 나누어 떨어진다.
# 100으로 나누어 떨어지면 연도는 윤년이 아니다.
# 400으로 나누어 떨어지면 윤년이다.

year = int(input("년도를 입력하세요 : "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # year을 100으로 나눴을 때 나머지가 0이 아니거나 400으로 나눴을 때 나머지가 0인 것 중에 4로 나눴을 때 나머지가 0인 것
    print(f"{year}은 윤년 입니다.")
else:
    print(f"{year}은 윤년이 아닙니다.")