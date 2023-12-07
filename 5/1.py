with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")
seeds = list(map(int,lines[0].split(":")[1].strip().split()))
# print(seeds)
i = 3

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

for seed in seeds:
    seed_to_soil[seed] = seed
    

while i < len(lines) and lines[i]:
    start, seed_start, step = tuple(map(int,lines[i].split()))
    for seed in seeds:
        if seed >= seed_start and seed < seed_start + step:
            seed_to_soil[seed] = start + (seed-seed_start)

    i+=1
# print(seed_to_soil)
i+=2
soils = seed_to_soil.values()
for soil in soils:
    soil_to_fertilizer[soil] = soil
while i < len(lines) and lines[i]:
    start, soil_start, step = tuple(map(int,lines[i].split()))
    for soil in soils:
        if soil >= soil_start and soil < soil_start + step:
            soil_to_fertilizer[soil] = start + (soil-soil_start)
    i+=1
i+=2

# print(soil_to_fertilizer)
fertilizers = soil_to_fertilizer.values()

for f in fertilizers:
    fertilizer_to_water[f] = f

while i < len(lines) and lines[i]:
    start, fertilizer_start, step = tuple(map(int,lines[i].split()))
    for f in fertilizers:
        if f >= fertilizer_start and f < fertilizer_start + step:
            fertilizer_to_water[f] = start + (f-fertilizer_start)
    i+=1

i+=2
# print(fertilizer_to_water)
waters = fertilizer_to_water.values()

for w in waters:
    water_to_light[w] = w

while i < len(lines) and lines[i]:
    start, l, step = tuple(map(int,lines[i].split()))
    for w in waters:
        if w >= l and w < l + step:
            water_to_light[w] = start + (w-l)
    i+=1
i+=2
# print(water_to_light)
lights = water_to_light.values()

for l in lights:
    light_to_temperature[l] = l

while i < len(lines) and lines[i]:
    start, t, step = tuple(map(int,lines[i].split()))
    for l in lights:
        if l >= t and l < t + step:
            light_to_temperature[l] = start + (l-t)
    i+=1
i+=2

# print(light_to_temperature)
temperatures = light_to_temperature.values()

for t in temperatures:
    temperature_to_humidity[t] = t

while i < len(lines) and lines[i]:
    start, h, step = tuple(map(int,lines[i].split()))
    for t in temperatures:
        if t >= h and t < h + step:
            temperature_to_humidity[t] = start + (t-h)
    i+=1

# print(temperature_to_humidity)

i+=2

humidities = temperature_to_humidity.values()

for h in humidities:
    humidity_to_location[h] = h

while i < len(lines) and lines[i]:
    start, l, step = tuple(map(int,lines[i].split()))
    for h in humidities:
        if h >= l and h < l + step:
            humidity_to_location[h] = start + (h-l)
    i+=1


print(min(humidity_to_location.values()))
# res = float("inf")
# for seed in seeds:
#     res = min(res,humidity_to_location[temperature_to_humidity[light_to_temperature[water_to_light[fertilizer_to_water[soil_to_fertilizer[seed_to_soil[seed]]]]]]])
# print(res)