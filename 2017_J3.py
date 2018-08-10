a,b = map(int, input().split(' '))
c,d = map(int, input().split(' '))
distance = abs(c-a) + abs(d-b)

t = int(input())

if distance == t or (((distance - t) % 2 == 0 and distance <= t)):
    print('Y')
else:
    print('N')
