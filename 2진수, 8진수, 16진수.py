print(bin(10))  #0b1010
print(oct(10))  #0o12
print(hex(10))  #0xa

print(format(10, 'b')) #1010
print(format(10, 'o')) #12
print(format(10, 'x')) #a 

print(int('1010',2))  #2진수 -> 10진수 변환: 10
print(int('12',8))    #8진수 -> 10진수 변환: 10
print(int('a',16))    #16진수 -> 10진수 변환 : 10 

#16진법 구구단 
x = input()
y = int(x, 16)
for i in range(1, 16):
    a = format(y*i, 'x')
    b = format(i, 'x')
    print(x+'*'+b+'='+a)
    
