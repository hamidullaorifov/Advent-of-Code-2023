from collections import defaultdict

with open('input.txt','r') as f:
    data = f.read().strip().split('\n')
nums_positions = []

gears = defaultdict(list)

for i, line in enumerate(data):
    # nums_length = 0
    num = ''
    j = 0
    while j<len(line):
        if line[j].isdigit():
            k = j
            while j < len(line) and line[j].isdigit() :
                num+=line[j]
                j+=1
            if num:
                nums_positions.append((num,i,k))
                num = ''
        j+=1
# print(nums_positions)



s = 0
for p in nums_positions:
    num, i, j = p
    is_part = False
    # gear = set()
    if j+len(num) < len(data[i]):
        ch = data[i][j+len(num)]
        if ch == "*":
            gears[(i,j+len(num))].append(num)
    if j > 0 and data[i][j-1]=='*':
        gears[(i,j-1)].append(num)
    if i > 0:
        if j > 0 and data[i-1][j-1]=='*':
            gears[(i-1,j-1)].append(num)
        if j + len(num) < len(data[i]) and data[i-1][j+len(num)]=='*':
            gears[(i-1,j+len(num))].append(num)
        # if data[i-1][j] != '.' or (j + len(num)-1<len(data[i]) and data[i-1][j+len(num)-1]!='.'):
        #     is_part = True
        for k in range(j,j+len(num)):
            if data[i-1][k] == '*':
                gears[(i-1,k)].append(num)
    if i < len(data)-1:
        if j > 0 and data[i+1][j-1]=='*':
            gears[(i+1,j-1)].append(num)
        if j + len(num) < len(data[i]) and data[i+1][j+len(num)]=='*':
            gears[(i+1,j+len(num))].append(num)
        # if data[i+1][j] !='.' or (j+len(num)-1 < len(data[i]) and data[i+1][j+len(num)-1] != '.'):
        #     is_part = True
        # else:
        #     print("A",num,i+1,j+1+len(num))
        for k in range(j,j+len(num)):
            if data[i+1][k] == '*':
                gears[(i+1,k)].append(num)
                
    
    # else:
    #     print(num,is_part)
for v in gears.values():
    if len(v)==2:
        s+=int(v[0])*int(v[1])
print(s)