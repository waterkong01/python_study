# 튜플은 시퀀스 자료형
# immutable(이뮤터블) : 읽기만 가능
# () 또는 괄호가 없으면 튜플
# 패킹과 어패킹 동작을 지원
person = "정택운", 33, "서울특별시 서초구 양재동서울특별시 서초구 양재동" # 패킹 (Packing)
print(type(person))

num = 1,
print(type(num)) # tuple

num = 1
print(type(num)) # int

name, age, addr = person # 언패킹 (Unpacking)
print(addr)

def get_person():
    name = "차학연"
    age = 34
    addr = "경상남도 창원시 성산구"
    return name, age, addr

info = get_person()
print(info)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# 합집합
print(s1.union(s2))
print(s1 | s2)
# 교집합
print(s1.intersection(s2))
print(s1 & s2)
# 차집합
print(s1.difference(s2))
print(s1 - s2)