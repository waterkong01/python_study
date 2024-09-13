# # 별찍기_기본
# n = int(input("정수 입력 : "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# 별찍기_가운데 정렬
n = int(input("정수 입력 : "))
ls = str(n)
for i in range(n):
    for j in range(i+1):
        print(f"{ls.count(str(i)) : n}", end="")
        # print("*", end="")
        # if i // n % 1:
        #     print()