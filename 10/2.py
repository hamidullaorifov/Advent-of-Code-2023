with open("test_input.txt",'r') as f:
    lines = f.read().strip().split('\n')

res = 0
dots = []
for i , line in enumerate(lines):
    for j, t in enumerate(line):
        if t == '.':
            dots.append((i,j))

left = 'L7F|'
for pos in dots:
    i,j = pos
    
    
    inner = False
    
    for k in range(i+1):
        if lines[k][j] != '.':
            inner = not inner

    if not inner:
        for k in range(j+1):
            if lines[i][k] in '':
                inner = not inner
    elif not inner:
        for k in range(i,len(lines)):
            if lines[k][j] != '.':
                inner = not inner
    elif not inner:
        for k in range(j,len(lines[0])):
            if lines[i][k] != '.':
                inner = not inner

    if inner:
        # print(pos)
        res += 1
print(res)

            
        
