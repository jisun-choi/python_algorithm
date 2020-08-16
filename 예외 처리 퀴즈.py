#8
class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while True:
    try:
        print(f'[남은 치킨: {chicken}]')
        order = int(input('치킨 몇 마리 주문?'))
        if order > chicken:
            print('재료 부족')
        elif order <= 0:
            raise ValueError
        else:
            print(f'[대기번호 {waiting}] {order} 마리 주문 완료')
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print('잘못된 값을 입력하였습니다.')
    except SoldOutError:
        print('재고 소진. 주문 불가')
        break