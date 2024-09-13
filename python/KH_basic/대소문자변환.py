# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
# for문 사용
# islower() : 소문자이면 True, 아니면 False
from networkx import write_edgelist

# 대소문자 바꾸기 : upper(), lower()

# e: element
# rst
rst = ""
for e in input("입력 : "):
    if e.islower():
        rst += e.upper() # rst = rst + e.upper()
    else:
        rst += e.lower()
print(rst)