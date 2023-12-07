with open('input.txt','r') as f:
    data = f.readlines()


    
             
s = 0
for row in data:
    required_cubes = {
        "red":0,
        "green":0,
        "blue":0
    }
    game, result = row.split(":")
    index = int(game.split()[1])
    sets = result.split(";")
    for st in sets:
        cubes = st.strip().split(",")
        for cube in cubes:
            count, color = cube.split()
            required_cubes[color] = max(required_cubes[color],int(count))
    p = 1
    for val in required_cubes.values():
        p*=val
    s+=p
print(s)

  
                    
