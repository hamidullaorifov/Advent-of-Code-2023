with open('input.txt','r') as f:
    data = f.readlines()
exist_cubes = {
    "red":12,
    "green":13,
    "blue":14
}

def isValid(sets):
    for st in sets:
        cubes = st.strip().split(",")
        for cube in cubes:
            count, color = cube.split()
            if int(count) > exist_cubes[color]:
                return False
    return True    
s = 0
for row in data:
    game, result = row.split(":")
    index = int(game.split()[1])
    sets = result.split(";")
    if isValid(sets=sets):
        s+=index

    
print(s)

  
                    
