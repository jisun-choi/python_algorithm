#datetime 모듈 연습 
import datetime

now = datetime.datetime.now()

output_a = now.strftime('%y.%m.%d.%H.%m')
output_b = f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분'
print(output_a)
print(output_b)

#특정 시간 교체하기 
output = now.replace(year = (now.year + 1))
print(output)

#특정 시간 이후 시간 구하기
after = now + datetime.timedelta(weeks = 1, hours = 1)
print(after)

#urilib 모듈 연습
from urllib import request 

target = request.urlopen('http://google.com')
output = target.read()

print(output)