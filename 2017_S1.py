N = int(input())
def SumList(lst):
    Sums = [lst[0]]
    for i in range(1,N):
        Sums.append(Sums[i-1] + lst[i])
    return Sums
same = False

Sw = input().split(' ')
Sem = input().split(' ')
intSw = list(map(int,Sw))
intSem = list(map(int,Sem))

sumSw = SumList(intSw)
sumSem = SumList(intSem)
# print(sumSw)
# print(sumSem)
for i in range(N-1,-1,-1):
    if sumSw[i] == sumSem[i]:
        print(i+1)
        same = True
        break

if same == False:
    print(0)
