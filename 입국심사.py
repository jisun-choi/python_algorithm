n = 6 
times = [7, 10]
count_1 = []
count_2 = []

for i in range(1, n // len(times)+1):
    count_1.append(times[0] * i)
    count_2.append(times[1] * i)
    if (times[1] * i) - (times[0] * i) > times[0]:
        count_1.append(times[0] * i + times[0])
        count_2.pop()

print('count_1',count_1)
print('count_2',count_2)
print(count_1[-1])




    
