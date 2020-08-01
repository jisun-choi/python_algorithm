def is_palindrome(a): 
    for i in range(len(a)//2):
        a_reverse = a[::-1]
        if a[:i] == a_reverse[:i]:
            continue    #이 자리에 True 값을 리턴할 경우 True 값이 하나라도 있으면 True 가 됨
        else:
            return False
            
a = input('word> ')

if is_palindrome(a) == None:
    print('True')
else:
    print(is_palindrome(a))
     
