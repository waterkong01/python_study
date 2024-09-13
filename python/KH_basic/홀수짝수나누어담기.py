# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력
num = list(map(int, input("숫자 입력 : ").split()))

# ver1
odd = list(filter(lambda x: x % 2 == 1, num))
even = list(filter(lambda x: x % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")

# ver2
even = []
odd = []
for e in num:
    if e % 2 == 0:
        even.append(e)
    else:
        odd.append(e)
print(f"홀수 : {odd}")
print(f"짝수 : {even}")