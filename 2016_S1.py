import sys
s1 = sys.stdin.readline()
s2 = sys.stdin.readline()


list1= [s1[i] for i in range(len(s1))]
list2 = [s2[i] for i in range(len(s2))]
ast = 0
for i in list2:
    if i == '*':
        ast += 1
        continue
    if i in list1:
        del(list1[list1.index(i)])
    else:
        print('N')
        break

if len(list1) == ast:
    print('A')
