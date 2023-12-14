
with open('input.txt','r') as f:
    grid = [list(line) for line in f.read().strip().split('\n')]




for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            k = i
            while k > 0 and grid[k-1][j] == '.':
                grid[k][j] = '.'
                k-=1
            grid[k][j] = 'O'




n = len(grid)
res = 0
for i in grid:
    count = 0
    for j in i:
        if j == 'O':
            count+=1
    
    # print(n,count)
    res += n*count
    n-=1

print(res)
    
