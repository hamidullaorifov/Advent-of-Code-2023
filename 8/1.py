with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

instruction = lines[0]

d = {}

for i in range(2,len(lines)):
    cur, lr = lines[i].split("=")
    # print(lr.strip(" ()").split(","))
    k = tuple(x.strip() for x in lr.strip(" ()").split(", "))
    d[cur.strip()] = k

step = 0
cur = 'AAA'
while cur != 'ZZZ':
    cur = d[cur][0] if instruction[step%len(instruction)] == 'L' else d[cur][1]
    step += 1

# right = True
# while cur != 'ZZZ':
#     cur = d[cur][1] if right else d[cur][0]
#     step += 1
#     right = not right

print(step)
    
