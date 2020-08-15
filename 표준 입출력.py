#표준 입, 출력
scores = {'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    print(subject.ljust(3), str(score).rjust(4), sep = ':')

for num in range(1, 21):
    print('대기번호:' + str(num).zfill(3))

#빈 자리는 빈공간으로 두고 오른쪽 정렬하고 10자리 공간 확보
print('{0: >10}'.format(500))

#왼쪽 정렬하고 빈칸 _로 채우기
print('{0:_<10}'.format(500))

#3자리 마다 콤마 찍어주기
print('{0:,}'.format(1000000000))

#3자리 마다 콤마 찍고, 부호 붙이고, 자릿수 확보, 빈자리는 ^로 채우기
print('{0:^<+30,}'.format(10000000000000))

#소수점 특정 자리수까지만 표시 
print("{0:.2f}".format(5/3))


 
