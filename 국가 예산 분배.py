#국가 전체 예산 M을 정하고, 4개 지방에서 요청하는 예산을 각 각 정한 후 국가 전체를 최대로 사용 할 수 있는 지방예산의 상한액을 정하는 프로그램을 작성하시오.

M = 500
list = {'a':225, 'b':100, 'c':350, 'd':105}
index_budget_list = []
paid = []

#딕셔너리 -> 리스트 변환 (인덱싱 하기 위해)
for i in range(1):
  for j in list.items():
    index_budget_list.append(j)

#총 예산 n분의 일 값보다 같거나 작은 수 찾아서 paid 에 집어넣기 / 클 경우 0 넣음
for o in range(4):
  if index_budget_list[o][1] <= (M // 4):
    paid.append(index_budget_list[o][1])
  else:
    paid.append(0)

#n분의 1보다 크거나 같은 값 지불하고 예산에서 삭제 후 나머지에게 줄 수 있는 최대 예산 계산
M = M - sum(paid)
budget = M //(paid.count(0))

#모든 요청이 배정될 수 없는 경우 
for l in range(4):
  if paid[l] != 0:
    print(index_budget_list[l][0],':%d 지급'% paid[l])
  else:
    print(index_budget_list[l][0],':예산 초과, %d 지급' %budget)
-----------------------------------------------------------------------------
#전부 그대로 지급할 수 있는 경우 
list = {'a':105, 'b':100, 'c':150, 'd':105}

budget_left = M - sum(paid)
over = []

for u in range(4):
  if paid[u] == 0:
    over.append(paid[u])
    if len(over) == 1:
      print(index_budget_list[u][0],':%d 지급'% index_budget_list[u][1])
    else:
      print(index_budget_list[u][0],':%d 지급'% budget)
  else:
    print(index_budget_list[u][0],':%d 지급'% paid[u])