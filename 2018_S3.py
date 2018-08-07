size = input().split(' ')
numRow = int(size[0])
numColumn = int(size[1])
EmptyCells = []
MovementGrid = []
cameras = []
ConDirections = 'UDLR'
ConMoves = [[-1,0],[1,0],[0,-1],[0,1]]
CheckedCells = [[5646544 for o in range(numColumn)] for p in range(numRow)]
ValidCells = [[True for i in range(numColumn)] for j in range(numRow)]
fy = 0
fx = 0

for i in range(numRow):
    MovementGrid.append(input())
    MovementGrid[i] = list(MovementGrid[i])
    for j in range(numColumn):
        if MovementGrid[i][j] == '.':
            EmptyCells.append([i,j])
        elif MovementGrid[i][j] == 'S':
            fx = j
            fy = i
        elif MovementGrid[i][j] == 'C':
            cameras.append([i,j])


for cell in cameras:

    y,x = cell[0],cell[1]
    ValidCells[y][x] = False
    for i in range(y, numRow):
        if MovementGrid[i][x] == 'W':
            break
        
        ValidCells[i][x] = False
    for i in range(y, -1,-1):
        if MovementGrid[i][x] == 'W':
            break
       
        ValidCells[i][x] = False
    for i in range(x, numColumn):
        if MovementGrid[y][i] == 'W':
            break
        
        ValidCells[y][i] = False
    for i in range(x,-1-1):
        if MovementGrid[y][i] == 'W':
            break
        
        ValidCells[y][i] = False


CellQueue = [[fy,fx]]
CheckedCells[fy][fx] = 0
if ValidCells[fy][fx] == True:
    while CellQueue:
        # print(CellQueue)
        #print(CheckedCells)
        y,x = CellQueue.pop(0)
        # print(y)
        # print(x)

        if MovementGrid[y][x] in ConDirections:
            y_new = y + ConMoves[ConDirections.find(MovementGrid[y][x])][0]
            x_new = x + ConMoves[ConDirections.find(MovementGrid[y][x])][1]
            # print(y_new)
            # print(x_new)
            if CheckedCells[y_new][x_new] > CheckedCells[y][x] and MovementGrid[y_new][x_new] != 'W':
                if MovementGrid[y_new][x_new] in ConDirections or ValidCells[y_new][x_new] == True:
                    CheckedCells[y_new][x_new] = CheckedCells[y][x]
                    CellQueue.append([y_new,x_new])
            continue
        #print(CheckedCells)
        if MovementGrid[y+1][x] != 'W' and CheckedCells[y+1][x] > CheckedCells[y][x]+1:
            #print(CheckedCells)
            if ValidCells[y+1][x] == True or MovementGrid[y+1][x] in ConDirections:
                CheckedCells[y+1][x] = CheckedCells[y][x]+1
                CellQueue.append([y+1,x])
                #print(CheckedCells)
        if MovementGrid[y-1][x] != 'W' and CheckedCells[y-1][x] > CheckedCells[y][x]+1:
            #print(CheckedCells)
            if ValidCells[y-1][x] == True or MovementGrid[y-1][x] in ConDirections:
                CheckedCells[y-1][x] = CheckedCells[y][x]+1
                CellQueue.append([y-1,x])
                #print(CheckedCells)
        if MovementGrid[y][x+1] != 'W' and CheckedCells[y][x+1] > CheckedCells[y][x]+1:
            #print(CheckedCells)
            if ValidCells[y][x+1] == True or MovementGrid[y][x+1] in ConDirections:
                CheckedCells[y][x+1] = CheckedCells[y][x]+1
                CellQueue.append([y,x+1])
                #print(CheckedCells)
        if MovementGrid[y][x-1] != 'W' and CheckedCells[y][x-1] > CheckedCells[y][x]+1:
            #print(CheckedCells)
            if ValidCells[y][x-1] == True or MovementGrid[y][x-1] in ConDirections:
                CheckedCells[y][x-1] = CheckedCells[y][x]+1
                CellQueue.append([y,x-1])
                #print(CheckedCells)

# print(CheckedCells)
# #print(MovementGrid)
# print(ValidCells)
# #print(fx)
# #print(fy)
# print(EmptyCells)


for cell in EmptyCells:
    if CheckedCells[cell[0]][cell[1]] == 5646544:
        print(-1)
    else:
        print(CheckedCells[cell[0]][cell[1]])








