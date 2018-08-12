Rows = []
Columns = [[],[],[],[]]
magic = True
for i in range(4):
    Rows.append(list(map(int,input().split(' '))))

Sum = sum(Rows[0])

for i in range(4):
    for j in range(4):
        Columns[i].append(Rows[j][i])

for i in range(4):
    if sum(Rows[i]) != Sum or sum(Columns[i]) != Sum:
        magic = False
        break


if magic:
    print('magic')
else:
    print('not magic')
