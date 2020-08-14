#if문 
weather = input('오늘 날씨 어때? ')
if weather == '비' or weather == '눈':
    print('우산을 챙기세요')
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('준비물 필요 없어요')

temp = int(input('오늘 기온은 어때? '))
if 30 <= temp:
    print('너무 더워요. 나가지 마세요')
elif 10 <= temp and temp <30:
    print('괜찮은 날씨에요')
elif 0 <= temp <10:
    print('외투를 챙기세요')
else:
    print('너무 추워요. 나가지 마세요')

#while문 
customer = '토르'
index = 5
while index >= 1:
    print(f'{customer}, 커피가 준비 되었습니다. {index}번 남았아요.')
    index -= 1
    if index == 0:
        print('커피는 폐기처분 되었습니다.')

#손님을 불렀을 때 커피를 받으러 온 손님이 맞아야 while문 종료
customer = '토르'
person = ''
while person != customer:
    print(f'{customer}, 커피가 준비 되었습니다.')
    person = input('이름이 어떻게 되세요?')

#컴프리핸션 
students = [1, 2, 3, 4, 5]
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환 (컴프리핸션)
students = ['Iron man', 'Thor', 'I am groot']
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환 (컴프리핸션)
students = ['Iron man', 'Thor', 'I am groot']
students = [i.upper() for i in students]
print(students)

#함수
def deposit(balance, money):
    print(f'입금 완료. 잔액은 {balance + money}')
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print(f'출금 완료. 잔액은 {balance - money}원')
        return balance - money
    else:
        print(f'출금 불가. 잔액은 {balance}원')
        return balance

def withdraw_night(balance, money):
    commission = 100
    print(f'수수료는 {commission}원. 잔액은 {balance - money - commission}원')
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)

print(balance)

#가변인자 
def profile(name, age, *language):
    print(f'이름: {name}\t나이: {age}\t', end='')
    for lang in language:
        print(lang, end='\t')

profile('유재석',30, 'python','java','c')


#전역변수 
gun = 10

# 전역변수를 받아서 함수 
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')

# 함수 값을 리턴하여 전역 변수 업데이트
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')
    return gun

print(f'전체 총: {gun}')
checkpoint(2)
gun = checkpoint_ret(gun, 2)
print(f'남은 총: {gun}')

