# 제어문 - 조건문과 반복문의 의미
from mpmath import scorergi

num = int(input("정수값 입력 : "))

if num > 100:
    print(f"{num}은 100보다 큽니다.")
elif num < 100:
    print(f"{num}은 100보다 작습니다.")
else:
    print(f"{num}은 100과 같습니다.")

# 실습문제
# 성적을 입력 받아서 0~100 사이가 아니면 성적을 잘못 입력했다고 출력
# 성적이 0~100 사이 이고,
# 90점 이상이면 "A",
# 80점 이상이면 "B",
# 70점 이상이면 "C",
# 60점 이상이면 "D",
# 나머지는 "F"

# 강사님.ver (2중)
score = int(input("성적을 입력하세요 : "))

if 0 <= score <= 100:
    if 90 <= score:
        print("A")
    elif 80 <= score:
        print("B")
    elif 70 <= score:
        print("C")
    elif 60 <= score:
        print("D")
    else:
        print("F")
else:
        print("성적을 잘못 입력하였습니다.")



# 강사님.ver2 (2중X)
score = int(input("성적을 입력하세요 : "))

if score < 0 or score > 100:
    print("성적을 잘못 입력하였습니다.")
    exit()

if 90 <= score:
        print("A")
elif 80 <= score:
        print("B")
elif 70 <= score:
        print("C")
elif 60 <= score:
        print("D")
else:
        print("F")



# 강사님.ver3 (반복문(while))
while True:
    score = int(input("성적을 입력하세요 : "))
    if 0 <= score <= 100:
        if 90 <= score:
            print("A")
        elif 80 <= score:
            print("B")
        elif 70 <= score:
            print("C")
        elif 60 <= score:
            print("D")
        else:
            print("F")
        break
    else:
        print("성적을 잘못 입력하였습니다.")

# 내꺼.....
# score = int(input("성적을 입력하세요 : "))
# if  90 <= score <= 100:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# elif 0 <= score < 60:
#     print("F")
# else:
#     print("성적을 잘못 입력하였습니다.")


# 세자리 정수를 입력 받아서 100의 자리, 10의 자리, 1의 자리로 나누어 담고
# 이 중 가장 큰 수 출력
# 몫과 나머지로 변수 할당
# if else문으로 값 비교
num = int(input("세자리 정수 입력 : "))

a = num // 100 # num을 100으로 나눈 몫
b = (num % 100) // 10 # num을 100으로 나눈 나머지를 10으로 나눈 몫
c = ((num % 100) % 10) // 1 # num을 100으로 나눈 나머지를 다시 10으로 나눈 나머지를 1로 나눈 몫
# c = num % 10 # 강사님.ver, num을 10으로 나눈 나머지, 위에 코드 보다 간결함

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)