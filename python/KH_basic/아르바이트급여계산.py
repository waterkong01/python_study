# 주/야간 근무시간을 입력 받아 아르바이트 급여 계산하기
# 주간 근무 시급 : 9860원
# 야간 근무 시급 : 주간 시급 * 1.5
# [입력] 주간 근무 [1], 야간 근무 [2]를 입력하세요 : 
# [입력] 근무 시간을 입력하세요 :
# [출력] {근무 시간} 동안 근무한 {주/야간} 급여는 {급여}원 입니다.

# 강사님.ver
work_type = int(input("주간근무 [1] 야간근무[2] 를 입력 하세요 : "))
# work_time = int(input("근무 시간을 입력 하세요 : "))
HOUR_PAY = 9860

if work_type == 1: # work_type(근무 타입)이 1일 때
    work_time = int(input("근무 시간을 입력 하세요 : "))
    pay = work_time * HOUR_PAY # pay는 work_time(근무 시간) * HOUR_PAY(시급)
elif work_type == 2: # work_type(근무 타입)이 1 이외의 수일 때
    work_time = int(input("근무 시간을 입력 하세요 : "))
    pay = work_time * HOUR_PAY * 1.5 # pay
else:
    print("근무 타입을 잘못 입력했습니다.")
    exit()

work_type_str = work_type == 1 and "주간" or "야간"
pay_str = f"{pay:,.0f}"
print(f"{work_time}시간 동안 근무한 {work_type_str} 급여는 {pay_str}원 입니다.")











# 내꺼.....실패
# day = "주간"
# night = "야간"
# d_p = "9860"
# d_n = int(input("주간 근무 [1] / 야간 근무 [2]를 입력하세요 : "))
# time = int(input("근무 시간을 입력하세요. : "))
# 
# if d_n == 1:
#     print(f"{time}시간 동안 근무한 {day} 급여는 {time * d_p}원 입니다.")
# elif d_n == 2:
#     print(f"{time}시간 동안 근무한 {night} 급여는 {time * d_p * 1.5}원 입니다.")
# else:
#     print(f"근무 타입을 잘못 입력하였습니다.")