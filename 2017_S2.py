N = int(input())
original = ''
randTide = sorted(list(map(int,input().split(' '))))

if N % 2 == 0:
    low = randTide[(N//2)-1::-1]
    high = randTide[N//2:N]

else:
    low = randTide[(N+1)//2-1::-1]
    high = randTide[(N+1)//2::]
    # print(len(low))
    # print(len(high))
for i in range(len(high)):

    original += str(low[i]) + ' '
    original += str(high[i]) + ' '

if len(low) > len(high):
    original += str(low[len(low)-1])

print(original)
