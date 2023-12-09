from math import lcm
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")



instruction = lines[0]

d = {}

for i in range(2,len(lines)):
    cur, lr = lines[i].split("=")
    k = tuple(x.strip() for x in lr.strip(" ()").split(", "))
    d[cur.strip()] = k

step = 0
curr_positions = tuple(x for x in d.keys() if x[-1]=='A')
finish = False
steps_toZ = [1]*len(curr_positions)
while not finish:
    left = instruction[step%len(instruction)] == 'L'
    next_positions = tuple(d[pos][0] if left else d[pos][1] for pos in curr_positions)
    curr_positions = next_positions
    step += 1
    for i,pos in enumerate(next_positions):
        if steps_toZ[i]==1 and pos[-1]=='Z':
            steps_toZ[i] = step
    finish = all(x != 1 for x in steps_toZ)

# right = True
# while cur != 'ZZZ':
#     cur = d[cur][1] if right else d[cur][0]
#     step += 1
#     right = not right

print(lcm(*steps_toZ))
    
