import sys
input = sys.stdin.readline

num_switch = int(input())
switch = list(map(int, input().split()))
num_student = int(input())
student = [list(map(int, input().split())) for _ in range(num_student)]

for i in range(num_student):
    is_man, pivot = student[i][0] == 1, student[i][1]

    if is_man:
        for j in range(pivot, num_switch+1, pivot):
            if switch[j-1] == 1:
                switch[j-1] = 0
            else:
                switch[j-1] = 1
    else:
        l, r = pivot-1, pivot-1
        while 0<l and r<num_switch-1:
            if switch[l-1] == switch[r+1]:
                l-= 1
                r+= 1
            else:
                break
                
        for k in range(l, r+1):
            if switch[k] == 1:
                switch[k] = 0
            else:
                switch[k] = 1

for i, state in enumerate(switch, start=1):
    print(state, end='')
    if i % 20 == 0:
        print()
    elif i != num_switch:
        print(' ', end='')