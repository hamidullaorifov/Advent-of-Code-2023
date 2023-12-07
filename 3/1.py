with open('input.txt','r') as f:
    data = f.read().strip().split('\n')
nums_positions = []


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
    if j+len(num) < len(data[i]) and data[i][j+len(num)]!='.' and not data[i][j+len(num)].isdigit():
        is_part = True
    if j > 0 and data[i][j-1]!='.' and not data[i][j-1].isdigit():
        is_part = True
    if i > 0:
        if j > 0 and not data[i-1][j-1].isdigit() and data[i-1][j-1]!='.':
            is_part = True
        if j + len(num) < len(data[i]) and data[i-1][j+len(num)]!='.' and not data[i-1][j+len(num)].isdigit():
            is_part = True
        # if data[i-1][j] != '.' or (j + len(num)-1<len(data[i]) and data[i-1][j+len(num)-1]!='.'):
        #     is_part = True
        for k in range(j,j+len(num)):
            if data[i-1][k] != '.' and not data[i-1][j+len(num)].isdigit():
                is_part = True
                break
    if i < len(data)-1:
        if j > 0 and data[i+1][j-1]!='.' and not data[i+1][j-1].isdigit():
            is_part = True
        if j + len(num) < len(data[i]) and data[i+1][j+len(num)]!='.' and not data[i+1][j+len(num)].isdigit():
            
            is_part = True
        # if data[i+1][j] !='.' or (j+len(num)-1 < len(data[i]) and data[i+1][j+len(num)-1] != '.'):
        #     is_part = True
        # else:
        #     print("A",num,i+1,j+1+len(num))
        for k in range(j,j+len(num)):
            if data[i+1][k] != '.' and not data[i+1][k].isdigit():
                is_part = True
                break
    if is_part:
        s+=int(num)
    # else:
    #     print(num,is_part)
print(s)