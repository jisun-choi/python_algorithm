goods = {'1.coke': 1000, '2.coffee': 1500, '3.water':700, '4.candy bar':1000, '5.jelly':800}
goods_name = list(goods.keys())
prices = list(goods.values())


count = 0
input_amount = int(input('금액을 넣어주세요> '))
user_input = int(input('물건을 선택하세요> ')) - 1 
pick_one = ['다시 선택', '돈 투입']

while count < 3:
    if input_amount < prices[user_input]:
        balance = prices[user_input] - input_amount
        pick = int(input(f'금액이 부족합니다. 1. 다른 음료를 선택 하시거나 2. {balance}원 더 넣으세요> '))
        if pick == 2: 
            input_amount = input_amount + int(input('금액을 넣어주세요> '))
            continue
        else:
            user_input = int(input('물건을 선택하세요> ')) - 1
            continue
    else:
        change = input_amount - prices[user_input]
        print(f'{goods_name[user_input]}을 받으세요. 남은 금액은 {change}입니다.')
        if count < 2: 
            ask = input('계속하시겠습니까?(Y/N) ')
            if 'Y' in ask: 
                input_amount = change
                user_input = int(input('물건을 선택하세요> ')) - 1
                count += 1
                continue
            else:
                print(f'잔돈을 받으세요. {change}원 입니다.')
                count += 1
        break
