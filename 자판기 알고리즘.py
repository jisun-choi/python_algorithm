#자판기 내의 음식이나 음료의 종류는 2가지 이상. (한번에 같은 음료 선택 가능)
#금액 투입 후, 잔돈을 계산 하는 알고리즘도 함께. (예: 1000원 투입 후, 300원짜리 선택하면, 700원이 남으므로 더 살 수 있게끔 짜주세요, 단 금액 투입 후 금액이 남더라도 최대 3가지만 선택)

v_machine = {'water':300,'coffee':500,'s.water':400,'coke':450,'fanta':350}
i = 1
input_amount = int(input('insert coins: '))
products = input('choose products: ')
change = input_amount - v_machine[products]

#돈 모자라면 못 뽑음  
while i < 3:
    if input_amount > v_machine[products]:
        print ('get your',products,'change: ',change) 
        input_amount = change
        products = input('choose products: ')
        change = input_amount - v_machine[products]
    elif input_amount < v_machine[products]:
        print('need more coins')
        break
    else:
        print ('get your',products,'change: ',change)
        break
    i += 1 
    if i >= 4:
      print('exit')

#모자란 돈을 더 넣어서 뽑는 경우 : 세 가지 선택 불가.. 
while i < 4:
    if input_amount > v_machine[products]:
        print ('get your',products,'change: ',change) 
        input_amount = change
        products = input('choose products: ')
        change = input_amount - v_machine[products]
    elif input_amount < v_machine[products]:
        need = v_machine[products] - input_amount
        print('need more coins: ',need)
        input_amount_second = int(input('insert more coins: '))
        input_amount = input_amount_second + input_amount
        change = input_amount - v_machine[products]   
    elif change == 0:
        print ('get your',products,'change: ',change)
        break

    i += 1 
    if i >= 4:
      print('exit')

#계속 뽑을 지 말지 선택
while i < 3:
    if input_amount > v_machine[products]:
        print ('get your',products,'change: ',change) 
        input_amount = change
        ask = input('anything else?(Y/N)')
        if ask == 'Y':
         i =+ 1 
        else:
         print ('get your',products,'change: ',change) 
         break
        products = input('choose products: ')
        change = input_amount - v_machine[products]
        
    elif input_amount < v_machine[products]:
        need = v_machine[products] - input_amount
        print('need more coins: ',need)
        input_amount_second = int(input('insert more coins: '))
        input_amount = input_amount_second + input_amount
        change = input_amount - v_machine[products]   
    elif change == 0:
        print ('get your',products,'change: ',change)
        break
    i += 1 
    if i >= 4:
      print('exit')