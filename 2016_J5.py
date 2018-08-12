import sys
case = sys.stdin.readline()[0]
min = False

if case == '1':
    min = True
N = int(sys.stdin.readline())
dmoj = sorted(list(map(int,sys.stdin.readline().split(' '))))
peg = sorted(list(map(int,sys.stdin.readline().split(' '))))

total = 0
if min:

    for i in range(N):

        total+=max(dmoj[i],peg[i])

else:
    for i in range(N):
        total+=max(dmoj[i],peg[N-1-i])

print(total)
