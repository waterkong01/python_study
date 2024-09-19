# 클로저 - 함수 안에 내부 함수를 구현하는 것
# 객체지향언어에서 생성된 객체 내부의 메서드가 필드를 참조하는 것과 유사

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc()
print(c(1), c(2), c(3), c(4))

# 콜백 기능 구현
import time
def perform_operation(x, y, callback):
    result = 0
    for i in range(x):      # x값 만큼 대기 이후 callback 함수 호출
        result += i + x + y
        time.sleep(1)
    callback(result)

# 콜백 함수 정의
def callback_function(result):
    print(f"Operation result is : {result}")

perform_operation(10, 20, callback_function)

# 데코레이터 - 함수의 앞뒤에 기능을 추가할 때 사용
import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return  decorated

@datetime_deco
def for_sum():
        sum = 0
        for i in range(1, 10000):
            sum += i
        print(sum)
for_sum()