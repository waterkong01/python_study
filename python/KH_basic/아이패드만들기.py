from datetime import datetime
import time      # sleep 함수 사용하기 위해서
from netrc import netrc

from astropy.units.quantity_helper.function_helpers import select
from numba.cuda import laneid

make_cnt = 0    # 전역 변수, 생산 대수를 구하기 위해서

# 공통 함수 : 유사한 함수의 반복적인 특성을 모아서 함수 형태로 만듦
def select_option(prompt, options):
    while True:     # 제대로된 입력값이 들어올 때까지 반복
        print(prompt)
        for idx, option in enumerate(options, start=1):     # 시퀀스 자료형, 시작값
            print(f"[{idx}] {option}")
        sel = input("선택하세요 : ")
        if sel in map(str, range(1, len(options) + 1)):     # 메뉴가 2개 존재한다면
            return sel

def choice_pad():
    return select_option("<<iPad Pro 구입하기>>", ("구입하기", "종료하기"))

def select_screen():
    return select_option("디스플레이 선택 : ", ("11인치", "13인치"))

def select_color():
    return select_option("컬러 선택 : ", ("스페이스 그레이", "실버"))

def select_memory():
    return select_option("메모리 선택 : ", ("128GB", "256GB", "512GB", "1TB"))

def select_network():
    return select_option("네트워크 선택 : ", ("Wi-Fi", "Wi-Fi+Cellular"))

def select_name_service():
    sel = select_option("각인 서비스 : ", ("신청", "미신청"))
    if sel == "1":
        return input("각인할 내용 입력 : ")
    return  "iPad Pro"

def make_ipad(screen, color, memory, network, name_service):
    global make_cnt
    make_cnt += 1       # 생산 대수 누적

    # 선택된 옵션에 대한 출력
    screen_options = ("", "11인치", "12.9인치")
    color_options = ("", "스페이스그레이", "실버")
    memory_options = ("", "128GB", "256GB", "512GB", "1TB")
    network_options = ("", "Wi-Fi", "Wi-Fi+Cellular")

    # 시리얼 넘버 만들기
    serial_screen = "11" if screen == "1" else "13"
    serial_network = "W" if network == "1" else "C"
    serial_date = datetime.today().strftime("%Y%m%d")
    serial_number = f"iPad{serial_screen}{serial_network}{serial_date}{make_cnt}"

    print("\n아이패드 제작중...")

    for i in range(1, 31):
        print(f"\r제작중...[{i * 100 // 30}%]", end='')
        time.sleep(1)       # 1초 대기

    print("\n\niPad Pro가 출고 되었습니다.")
    print("=" * 34)
    print(f"화면 크기 : {screen_options[int(screen)]}")
    print(f"색상 : {color_options[int(color)]}")
    print(f"용량 : {memory_options[int(memory)]}")
    print(f"네트워크 : {network_options[int(network)]}")
    print(f"이름 : {name}")
    print(f"시리얼 넘버 : {serial_number}")
    print("-" * 34)

while True:
    if choice_pad() == "2":
        print("iPad Pro 구입을 종료합니다.")
        break

    screen = select_screen()
    color = select_color()
    memory = select_memory()
    network = select_network()
    name = select_name_service()
    make_ipad(screen, color, memory, network, name)