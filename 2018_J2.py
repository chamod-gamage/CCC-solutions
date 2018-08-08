N = int(input())
d1 = list(input())
d2 = list(input())
parked = 0
for i in range(N):
    if d1[i] == d2[i] and d1[i] == 'C':
        parked += 1

print(parked)
