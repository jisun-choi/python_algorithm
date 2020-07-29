#n 개의 100 이하의 자연수를 입력하고, 그 수들의 최소 공배수를 구하시오.

n = 3 

num_1 = int(input('num1?'))
num_2 = int(input('num2?'))
num_3 = int(input('num3?'))
list = [num_1, num_2, num_3]
results = max(list)

while results:
    if results % num_1 == 0 and results % num_2 == 0 and results % num_3 == 0:
        print('최소 공배수: ',results)
        break
    results += 1

#map 함수 사용하여 간결하게 고친 코드 
n = 3

nums = list(map(int, input('num?').split()))
results = max(nums)

while results:
    if results % nums[0] == 0 and results % nums[1] == 0 and results % nums[2] == 0:
        print('최소 공배수: ',results)
        break
    results += 1
