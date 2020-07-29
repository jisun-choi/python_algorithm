#파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력

list = ['intra.h', 'intra.c', 'define.h', 'run.py']
new_list = []

#list 값을 .을 기준으로 split 해서 new_list 에 담음 (2차원 리스트로 담긴다)
for i in range(len(list)):
    new_list.append(list[i].split('.'))
    i += 1

#new_list 위치 값에서 h 와 c 가 있는지 찾아보고 있으면 다시 join 으로 묶어서 프린트..
for o in range(len(list)):
    if 'h' in new_list[o]:
        print ('.h 확장자: ','.'.join(new_list[o]))

    if 'c' in new_list[o]:
        print ('.c 확장자: ','.'.join(new_list[o]))


#in 연산자 활용
for i in list:
    if '.h' or '.c' in list:
        print(i)