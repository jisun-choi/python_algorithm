#금액을 입력하면 화폐나 동전 몇 장(개)씩 필요한지 계산 하는 코드를 작성하시오.(예: 65,000원 = 5만원권 (1), 1만원권 (1), 5천원권 (1)
# 지폐 단위만 작성 
i = int(input('금액을 입력:'))
amount1 = i // 50000
var1 = i - (amount1*50000)
amount2 = var1 // 10000
var2 = i - (amount1*50000) - (amount2*10000)
amount3 = var2 // 5000
var3 = i - (amount1*50000) - (amount2*10000) - (amount3*5000)
amount4 = var3 // 1000
print (i,'원','=','5만원',amount1,'장,','1만원',amount2,'장,','5000원',amount3,'장,','1000원',amount4,'장')


#할당 연산자 %= 를 사용할 것 
