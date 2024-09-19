# 함수로 영화표 예매
# 사용자로부터 좌석 번호를 입력받아 예매하는 시스템, 좌석은 10개
# 예매가 완료되면 해당 좌석값을 1로 변경 (초기값은 0)
# 이미 예매가 완료된 좌석은 구매 불가
# 좌석당 가격은 12000원
# 프로그램 종료 시 매출액을 출력
from twisted.spread.jelly import set_atom

seat = [0] * 10     # 0으로 초기화된 10개의 리스트 생성
PRICE = 12000

def print_seat():
    for e in seat:
        if e == 0:
            print("[ ]", end=" ")
        else:
            print("[V]", end=" ")
    print()

def select_seat():
    print_seat()
    num = int(input("좌석 번호 입력 : ")) - 1     # 사용자의 입력 1부터 시작, 리스트 인덱스 0부터 시작
    if seat[num] == 0:
        seat[num] = 1       # 예약이 안된 좌석이므로 예약 진행
        print_seat()
    else:
        print("이미 예약된 좌석입니다.")

def total_account():
    cnt = 0     # 판매된 좌석의 수 누적
    for e in seat:
        if e == 1:
            cnt += 1
    return PRICE * cnt      # 티켓 가격 * 판매 좌석 수

while True:
    print("[1] 예매하기")
    print("[2] 종료하기")
    sel = int(input("메뉴 선택 : "))
    if sel == 1:
        select_seat()
    else:
        print(f"총 매출액 : {total_account()}원")
        break