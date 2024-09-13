# 리스트 : 연속적으로 저장되는 형태의 자료형
# 배열과 다르게 크기 지정 필요X
# 읽고 쓰기 가능 (뮤터블)
# 같은 자료형일 필요X
# [ ] (대괄호)로 표시

number = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, 10, 100, "apple", False, ["seoul", "korea"], ["차학연", "정택운", "이재환", "한상혁"]]

print(number)
print(fruits[1])
print(f"빅스 멤버 : {mixed[6]}")
print(f"{mixed[5][1]}")
print(f"{mixed[3][3]}") # 'mixed'의 'apple'의 'l'
print(f"{mixed[1:5]}")
print(f"{mixed[6][:2]}") # 'mixed'의 '["차학연", "정택운", "이재환", "한상혁"]'의 ['차학연', '정택운']
print(f"{mixed[6][1]}") # 'mixed'의 '["차학연", "정택운", "이재환", "한상혁"]'의 '정택운'

# 리스트 연산자 : +, *
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b) # [1, 2, 3, 4, 5, 6]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(a * b) # 오류

# 리스트 요소 추가 : append(), insert()
# append(값) : 리스트의 마지막에 값 추가
# insert(인덱스, 값) : 해당 위치에 값 추가

c = [3, 5, 7, 7]
c.append(9)
print(c)
c.append(99)
print(c)
c.insert(0, 1)
print(c)

# 리스트 제거 : pop, remove, clear
# pop() : 인덱스를 쓰지 않으면 마지막 인덱스 값을 반환하고 삭제
# 인덱스를 넣으면 해당 인덱스의 값 삭제 후 보여줌
print(c.pop())
print(c.pop(0))
print(c)

# remove(값) : 해당하는 값 삭제, 값이 여러개인 경우 인덱스가 낮은 것부터 삭제
c.remove(7)
print(c)

# del : 인덱스로 값 삭제
del c[0]
print(c)

# clear() : 리스트 내의 모든 내용을 삭제하고 빈 리스트만 남김
c.clear()
print(c)

# 중복 제거
list_double = ["A", "B", "C", "D", "A", "C"]
list_new = []
for e in list_double:
    if e not in list_new:
        list_new.append(e)
print(list_new)

# 리스트의 순회
names = ["차학연", "정택운", "이재환", "한상혁"]
for name in names:
    print(f"빅스 멤버 : {name}", end=" ")
print()

for i in range(len(names)):
    print(f"빅스 멤버 : {names[i]}", end=" ")