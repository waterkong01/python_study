# 주석은 인터프리터가 번역 하지 않는 영역
# 범위 주석: """     """
print("파이썬을 공부하겠습니다.") # 이 부분은 주석 입니다.
print(100) # 정수값 출력
print(33.3333) # 실수값 출력
print(100 + 200) # 연산자 사용
print(100 < 200) # True

# 파이썬은 값이 대입될 때 데이터형이 결정됨.
# "", '' 둘 다 문자열을 의미, 파이썬은 문자를 따로 구분하지 않음
# == 같다 / = 값을 변수에 대입
name = "사막여우"
print(name)

"""
 * 식별자 생성 규칙
 * 키워드(예약어) 사용 금지
 * 특수문자는 _(언더바)만 사용 가능
 * 숫자는 사용가능하지만 앞에 오면 안됨 (ex. 1sample)
 * snake_case : 스네이크 표기법, 단어와 단어를 연결할 때 사용
"""

name = "하수빈"
email = 'gioremo615@gmail.com'
phone = "010-4139-4711"
addr = "서울시 강북구 도봉로"

print(f"""
    이름 : {name}
    이메일 : {email}
    전화번호 : {phone}
    주소 : {addr}
""")