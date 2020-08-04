Age = {'A':20, 'B': 16, 'C': 30, 'D': 23}
Lit = {'A':90, 'B': 47, 'C': 30, 'D': 76}
Eng = {'A':86, 'B': 39, 'C': 64, 'D': 84}
Math = {'A':47, 'B': 52, 'C': 58, 'D': 73}

#C의 총점, 평균 
total = Lit['C']+Eng['C']+Math['C']
avg = total / 3

#나이 합계
age = Age.values()
print(sum(age))

#가장 적은 점수 
min_list = min(Lit.values()), min(Eng.values()), min(Math.values())
min_grade = min(min_list)
print(min_grade)



