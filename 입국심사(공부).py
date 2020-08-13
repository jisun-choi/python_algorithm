#수현님 아이디어, 프로그래머스 30점

times = [5, 3, 7] #검사관의 수 및 각자의 검사 시간
plus = [] 
n = 10 #검사를 받는 사람의 수
for i in range(len(times)):
    for j in range(1,n):
        plus.append(times[i]*j)
k = sorted(plus)
print(k)
print(k[n-1])


#이분탐색법: 탐색 범위를 반씩 줄인다.       
times = [5, 3, 7] #검사관의 수 및 각자의 검사 시간
n = 10 #검사를 받는 사람의 수

mintime = int(min(times) * n / len(times))
maxtime = int(max(times) * n / len(times))
while mintime != maxtime:
    target_time = (mintime + maxtime) // 2
    pass_num = sum([target_time // time for time in times]) - n
    print('min {}, target {}, max {}, pass {}'.format(mintime, target_time, maxtime, pass_num))
    if pass_num >= 0:
        maxtime = target_time
    else:
        mintime = target_time
    if maxtime - mintime == 1:
        break
print(maxtime)