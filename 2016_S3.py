import sys
sys.setrecursionlimit(167869690)
numrest,numpho = map(int,sys.stdin.readline().split(' '))
phonums = list(map(int,sys.stdin.readline().split(' ')))

phobool = [False for i in range(numrest)]
ends = [True for j in range(numrest)]
nodes = [False for k in range(numrest)]
ways = [[] for l in range(numrest)]
finaldist = 0
dis = [1 for m in range(numrest)]
index = [n for n in range(numrest)]
maxdist = 0


def subtrees(cur, pre):

    if phobool[cur] and not nodes[cur]:

        global finaldist
        finaldist += 2
        nodes[cur] = True

    for i in range(len(ways[cur])):
        if pre != ways[cur][i]:

            subtrees(ways[cur][i], cur)
            if nodes[ways[cur][i]] and not nodes[cur]:
                nodes[cur] = True

                finaldist += 2
def search1(cur,pre,dist):

    for i in range(len(ways[cur])):

        if nodes[ways[cur][i]] and ways[cur][i] != pre:
            search1(ways[cur][i], cur, dist+1)
            if dis[ways[cur][i]]>=dis[cur]:
                dis[cur] = dis[ways[cur][i]]+1
                index[cur] = index[ways[cur][i]]

def search2(cur,pre,dist):
    global maxdist
    if dist > maxdist:
        maxdist = dist
    for i in range(len(ways[cur])):

        if nodes[ways[cur][i]] and ways[cur][i] != pre:
            search2(ways[cur][i],cur,dist+1)

for i in range(numpho):
    phobool[phonums[i]] = True



for i in range(numrest-1):
    ai,bi = map(int,sys.stdin.readline().split(' '))
    ways[ai].append(bi)
    ways[bi].append(ai)


subtrees(phonums[0],-1)
search1(phonums[0],-1,0)
search2(index[phonums[0]],-1,0)


tot = finaldist-maxdist-2
print(tot)
