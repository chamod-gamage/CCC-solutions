import time
# import gspread

start = time.clock()
N = int(input())
def balancer(weight):
    if weight == 1:
        return weight
    numTrees = 0
    possible = []
    for i in range(weight):
        possible.append(True)

    for w in range(weight, 1, -1):
        if True not in possible:
            break
        for k in range(weight, 1, -1):
            if True not in possible:
                break
            if w % k == 0 and possible[k-1] == True:
                numTrees += balancer(w//k)
                possible[k-1] = False

    return numTrees

to_print = balancer(N)
print(to_print)
#########
#DUE TO THE TIME TAKEN BY RECURSION, THIS WILL TAKE TOO LONG FOR MOST CASES WHERE N > 2000.
##########
#finish=time.clock()
#print(str(finish-start))
#file = open("treetimer.txt","a+")
#file.write("A tree of weight " + str(N) + " has " + str(to_print) + " possibilities and took " + str(finish-start) + " seconds to complete.\r\n" )
#file.write("\n")
#file.close()

