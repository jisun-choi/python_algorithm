
# 문자열로 이루어진 리스트에서 각 요소의 n번째 글자를 뽑아 
# {문자열:n번째 글자} 딕셔너리로 만든다. 
def sort_strings(strings, n):
    check = {}
    for i in range(len(strings)):
        check[strings[i]] = strings[i][n]
    return check 

strings =['sun', 'bed', 'car']
checklist = sort_strings(strings, 1)

# 딕셔너리에서 값을 기준으로 오름차순 정렬 
print(sorted(checklist.keys(), key = lambda item : item[1]))


#좋은 예 (함수로 아예 리턴받기)
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))
