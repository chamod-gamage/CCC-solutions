N = int(input())
pages = []
finished = "N"
checked = []
shortest = 1234567890

for i in range(N):
    inputs = input()
    pages.append(inputs.split(' '))

# print(pages)

for i in range(len(pages)):
    for j in range(len(pages[i])):
        pages[i][j] = int(pages[i][j])

#
# print(pages)
for i in range(len(pages)):
    checked.append(1234567890)
    pages[i].append(i)
# print(pages)



checked[0] = 1

PageQueue = [pages[0]]

while PageQueue:

    page = PageQueue.pop(0)
    # print(page)
    # print(page[0])
    if page[0] != 0:
        for i in range(page[0]):
            if checked[page[i+1]-1] > checked[pages.index(page)] + 1:
                PageQueue.append(pages[page[i+1]-1])
                checked[page[i+1]-1] = checked[pages.index(page)] + 1


    # print(checked)
    # print(checked)
    if 1234567890 not in checked:

        finished = "Y"
        break




for i in range(len(pages)):
    if pages[i][0] == 0 and checked[i] < shortest:
        # print(i)
        shortest = checked[i]

print(finished)
print(shortest)

