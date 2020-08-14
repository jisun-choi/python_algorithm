#1
from random import *

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" +str(date) + "일로 선정되었습니다.")

#2
url = "http://naver.com"
my_str = url.replace("http://","") #http를 제거 
my_str = my_str[:my_str.index('.')]  #처음 만나는 . 이후 부분 제거 
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) +'!'
print(f'{url}의 비밀번호는 {password}입니다.')

#3
from random import * 
users = list(range(1, 21))
shuffle(users)
winners = sample(users, 4)

print(' -- 당첨자 발표 -- ')
print(f'치킨 당첨자 : {winners[0]}')
print(f'커피 당첨자 : {winners[1:]}')
print(' -- 축하합니다 -- ')

#4 
from random import *
cnt = 0  #총 탑승 승객 수 
for i in range(1, 51):   #1~50명 승객
    time = randrange(5, 51)  #5~50분 소요시간
    if 5 <= time <= 15:  #매칭 성공
        print(f'[o]{i}번째 손님 (소요시간 : {time}분)')
        cnt += 1 
    else:  #매칭 실패 
        print(f'[]{i}번째 손님 (소요시간 : {time}분)')

print(f'총 탑승 승객: {cnt}명')

#5 
def std_weight(height, gender):
    if gender == 'male':
        return height * height * 22
    else:
        return height * height * 21

height = 161
gender = 'female'

weight = round(std_weight(height / 100, gender),2)
print(f'키 {height}cm 의 표준 체중은 {weight}kg 입니다.')