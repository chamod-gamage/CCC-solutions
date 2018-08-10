mins = int(input())

from math import floor
def arithmetic(time):
    if time[0] == 0:
        if time[3] - time[2] == time[2] - time[1]:
            return True

        return False
    else:
        if time[3] - time[2] == time[2] - time[1] and time[1] - time[0] == time[2] - time[1]:
            return True


def find_seq(minutes):
    sum = 0
    h1 = 1
    h2 = 2
    m1 = 0
    m2 = 0
    for i in range(minutes):
        m2 += 1
        if m2 == 10:
            m2 = 0
            m1 += 1
            if m1 == 6:
                m1 = 0
                h2 += 1
                if h1 == 0 and h2 == 10:
                    h2 = 0
                    h1 += 1
                elif h1 == 1 and h2 == 3:
                    h2 =1
                    h1 = 0

        if arithmetic([h1,h2,m1,m2]):
            # print([h1,h2,m1,m2])
            sum += 1
    return(sum)

if mins<720:
    instances = find_seq(mins)
else:
    instances = floor(mins/720)*31 + find_seq(mins%720)

print(instances)
