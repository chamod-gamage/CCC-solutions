user = input()
stri = '0 ' + user

trip = stri.split(' ')

for i in range(len(trip)):
    trip[i] = int(trip[i])
sums = []
sum = 0
for i in range(len(trip)):
    sum += trip[i]
    sums.append(sum)


table=[]
for i in range(len(trip)):
    table.append([])
    for j in range(len(trip)):
        distance = max(sums[j]-sums[i], (sums[j]-sums[i])*-1)
        table[i].append(distance)



for i in table:
    for j in range(len(i)-1):
        print(i[j], end=' ')

    print(i[len(i)-1])

