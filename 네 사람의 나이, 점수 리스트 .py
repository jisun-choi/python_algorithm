#A, B, C, D 인 네 사람의 나이 및 국어, 영어, 수학 점수가 포함된 리스트를 작성
#모두의 나이의 합계, 모든 점수 중 가장 낮은 점수,C의 총점과 평균

#리스트 안의 나이, 점수 전부 자연수라는 가정 하에 작성 
Age= [aA,bA,cA,dA]
Lit= [aL,bL,cL,dL]
Eng=[aE,bE,cE,dE]
Math= [aM,bM,cM,dM]
Li = [Age,Lit,Eng,Math]

sum (Age) # 모두의 나이 합계 

grades = del Li[0]
min (grades) # 모든 점수 중 가장 낮은 점수 

C = Lit[2],Eng[2],Math[2]
sum (C) #C의 총점 
sum (C) / len(C) #C의 합계 
