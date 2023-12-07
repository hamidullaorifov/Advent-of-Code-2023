with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")
seeds = list(map(int,lines[0].split(":")[1].strip().split()))
# print(seeds)
# seeds = []
# for i in range(0,len(nums),2):
#     seeds.extend(range(nums[i],nums[i]+nums[i+1]))

# print(seeds)
i = 3
# total_seeds



    
soils = []
while i < len(lines) and lines[i]:
    soils.append(tuple(map(int,lines[i].split())))
    i+=1

i+=2

fertilizers = []
while i < len(lines) and lines[i]:
    fertilizers.append(tuple(map(int,lines[i].split())))
    i+=1
i+=2


waters = []
while i < len(lines) and lines[i]:
    waters.append(tuple(map(int,lines[i].split())))
    i+=1

i+=2

lights = []
while i < len(lines) and lines[i]:
    lights.append(tuple(map(int,lines[i].split())))
    i+=1
i+=2


temperatures = []

while i < len(lines) and lines[i]:
    temperatures.append(tuple(map(int,lines[i].split())))
    i+=1
i+=2


humidities = []

while i < len(lines) and lines[i]:
    humidities.append(tuple(map(int,lines[i].split())))
    i+=1

# print(temperature_to_humidity)

i+=2




locations = []
while i < len(lines) and lines[i]:
    locations.append(tuple(map(int,lines[i].split())))
    i+=1

def is_reachable_seed(seed):
    for i in range(0,len(seeds),2):
        if seed >=seeds[i] and seed < seeds[i] + seeds[i+1]:
            return True 
    return False

def is_reachable_soil(soil):
    for f  in soils:
        if soil >= f[0] and soil < f[0] + f[2]:
            seed = f[1] + soil - f[0]
            return is_reachable_seed(seed)
    return is_reachable_seed(soil)

def is_reachable_fertilizer(fer):
    for f  in fertilizers:
        if fer >= f[0] and fer < f[0] + f[2]:
            soil = f[1] + fer - f[0]
            return is_reachable_soil(soil)
    return is_reachable_soil(fer)

def is_reachable_water(water):
    for w  in waters:
        if water >= w[0] and water < w[0] + w[2]:
            fertilizer = w[1] + water - w[0]
            return is_reachable_fertilizer(fertilizer)
    return is_reachable_fertilizer(water)

def is_reachable_light(light):
    for l  in lights:
        if light >= l[0] and light < l[0] + l[2]:
            water = l[1] + light - l[0]
            return is_reachable_water(water)
    return is_reachable_water(light)

def is_reachable_temperature(temp):
    for t  in temperatures:
        if temp >= t[0] and temp < t[0] + t[2]:
            light = t[1] + temp - t[0]
            return is_reachable_light(light)
    return is_reachable_light(temp)


def is_reachable_humidity(hum):
    for h in humidities:
        if hum >= h[0] and hum < h[0] + h[2]:
            temperature = h[1] + hum - h[0]
            return is_reachable_temperature(temperature)
    return is_reachable_temperature(hum)

def is_reachable_location(loc):
    for l in locations:
        if loc >= l[0] and loc < l[0]+l[2]:
            humidity = l[1] + loc - l[0]
            return is_reachable_humidity(humidity)
    return is_reachable_humidity(loc)


max_loc = 0

for loc in locations:
    max_loc = max(max_loc,loc[0]+loc[2])
for i in range(max_loc):
    if is_reachable_location(i):
        print(i)
        break