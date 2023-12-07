from math import sqrt,ceil,floor
times = [61,67,75,71]
distances = [430,1036,1307,1150]
# times = [7,15,30]
# distances = [9,40,200]

res = 1
for t,d in zip(times,distances):
    D = sqrt(t*t - 4 * d)
    top = ceil((t+D)/2-1)
    bottom = floor((t-D)/2+1)
    res*=(top-bottom+1)

print(res)