sum = 0
for i in range(6):
    if input() == 'W':
        sum += 1
if sum == 0:
    print(-1)
elif sum > 4:
    print(1)
elif sum > 2:
    print(2)
else:
    print(3)
