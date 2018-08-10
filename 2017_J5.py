N= int(input())
Lengths = [0 for i in range(2001)]
for i in list(map(int, input().split(' '))):
    Lengths[i] += 1
def HeightBoards(height):
    lens = Lengths.copy()
    b1 = max(height-2000,1)
    b2 = height - b1
    numboards = 0
    for i in range(b1, height//2+1):
        if lens[b1] != 0 and lens[b2] != 0:
            if b1 == b2 and lens[b1] > 1:
                boards = lens[b1]/2 - max(0,(lens[b1] % 2)/2)
                lens[b1] -= boards*2
                numboards += boards
            elif b1 != b2:
                boards = min(lens[b1],lens[b2])
                lens[b1] -= boards
                lens[b2] -= boards
                numboards += boards
        b1+= 1
        b2-=1
    return numboards
max_b = 0
hmax = 0
for i in range(2,4001):
    Boards = HeightBoards(i)
    if Boards > max_b:
        max_b = Boards
        hmax = 1
    elif Boards == max_b:
        hmax += 1
print(str(int(max_b)) + ' ' + str(hmax))
#Removing spacing resulted in making the program run under 2 seconds for all test cases XD
