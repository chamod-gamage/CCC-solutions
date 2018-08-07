numVillages = int(input())
VillageList = []
HoodList = []

for i in range(numVillages):
    VillageList.append(int(input()))
VillageList = sorted(VillageList)

for i in range(1,len(VillageList)-1):
    left = (VillageList[i]-VillageList[i-1])/2
    right = (VillageList[i+1]-VillageList[i])/2
    hoodsize = (round(((left + right)*10)))/10
    HoodList.append(hoodsize)

HoodList.sort()
print(HoodList[0])
