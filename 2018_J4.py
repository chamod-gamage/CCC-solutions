TableSize = int(input())
Rows = []
IncRight = False
IncDown = False
Rowstring = []
for i in range(TableSize):
    Rows.append(input())

for i in range(TableSize):
    row = Rows[i].split()

    for j in range(len(row)):
        row[j] = int(row[j])
    if row[1] > row[0]:
        IncRight = True
    Rows[i] = row


if Rows[0][0] < Rows[1][0]:
    IncDown = True

if IncRight ==True and IncDown == True:
    for i in range(len(Rows)):
        Rowstring.append('')
        for j in range(len(Rows[i])):
            Rowstring[i]+=str(Rows[i][j])
            Rowstring[i] += ' '
        print(Rowstring[i])

if IncRight == False and IncDown == True:
    for i in range(TableSize):
        Rowstring.append('')
        for j in range(TableSize):
            Rowstring[i] += str(Rows[j][TableSize-1-i])
            Rowstring[i] += ' '
        print(Rowstring[i])

if IncRight == False and IncDown == False:
    for i in range(TableSize):
        Rowstring.append('')
        for j in range(TableSize):
            Rowstring[i] += str(Rows[TableSize-1-i][TableSize-1-j])
            Rowstring[i] += ' '
        print(Rowstring[i])

if IncRight == True and IncDown == False:
    for i in range(TableSize):
        Rowstring.append('')
        for j in range(TableSize):
            Rowstring[i] += str(Rows[TableSize-1-j][i])
            Rowstring[i] += ' '
        print(Rowstring[i])
