H,M = list(map(int,input().split(':')))
t = H + M/60
trip = 0

if t <= 5 or t >= 10 and t <= 13 or t >= 19:
    t = (t + 2)%24
    trip = 1

elif t < 7:

    trip = (7-t)*0.5
    t = 7

    if (1 - trip)*4 <= 3:

        t += (1-trip) * 4
        trip = 1
    else:

        t = 10
        trip += 0.75

        t += (1-trip)*2
        trip = 1
elif t >= 7 and t < 10:
    trip = (10-t)*0.25
    t = 10
    t += (1-trip) * 2
    trip = 1
elif t > 13 and t < 15:
    trip = (15-t)*0.5
    t = 15
    t += (1 - trip)*4
    trip = 1
elif t >= 15:
    trip = (19 - t)*0.25
    # print(trip)
    t = 19
    t += (1-trip)*2
    trip = 1
# print(t)
nM = int((t % 1)*60+1)
# print(nM)
nH = int((t - (t%1))%24)
# print(nH)
nM = round(nM/10)*10
if nH < 10:
    nH = '0' + str(nH)
if nM < 10:
    nM = '0' + str(round(nM))
nH = str(nH)
nM = str(nM)
print(nH + ':' + nM)







