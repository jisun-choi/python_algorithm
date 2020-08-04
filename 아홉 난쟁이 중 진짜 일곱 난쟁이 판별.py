# 진짜 일곱 난쟁 키 = [10, 15, 20, 5, 26, 11, 13]
# 9명 난쟁 키 리스트 = [10, 17, 15, 20, 21, 5, 26, 11, 13]

import itertools
import sys

# height = [int(input('난쟁이 키 입력')) for height in range(9)]
height = []
for i in range(9):
    height.append(int(sys.stdin.readline()))
total = sum(height)
correct = list(itertools.combinations(height,7))

for i in correct:
  if sum(i) == 100:
      a = list(i)
      break
for i in a:
    print(i)

